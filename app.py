"""
Medical Image Processing Web Application
A simple Flask application for processing X-ray images with various image processing techniques.
Features:
- Image upload (JPG, PNG)
- Grayscale conversion
- Histogram equalization (contrast enhancement)
- Gaussian blur
- Canny edge detection
- ZIP download of all results
"""

from flask import Flask, render_template, request, send_file, jsonify
import cv2
import numpy as np
import os
from datetime import datetime
import zipfile
from pathlib import Path

# Initialize Flask app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB

# Create required directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE


def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_medical_image(image_path, output_prefix):
    """
    Process medical image through multiple processing steps.
    
    Args:
        image_path (str): Path to the original image
        output_prefix (str): Prefix for output image filenames
        
    Returns:
        dict: Dictionary containing paths to all processed images
    """
    try:
        # Verify image file exists
        if not os.path.exists(image_path):
            raise ValueError(f"Image file not found: {image_path}")
        
        # Read the original image in color
        original = cv2.imread(image_path)
        if original is None:
            raise ValueError(f"Failed to read image. The file may be corrupted or in an unsupported format.")
        
        # Verify image dimensions
        if original.shape[0] == 0 or original.shape[1] == 0:
            raise ValueError("Image has invalid dimensions")
        
        # Save original image
        original_output = os.path.join(OUTPUT_FOLDER, f'{output_prefix}_original.png')
        success = cv2.imwrite(original_output, original)
        if not success:
            raise ValueError(f"Failed to save original image to {original_output}")
        
        # Convert to grayscale
        grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        grayscale_output = os.path.join(OUTPUT_FOLDER, f'{output_prefix}_grayscale.png')
        cv2.imwrite(grayscale_output, grayscale)
        
        # Apply histogram equalization (contrast enhancement)
        enhanced = cv2.equalizeHist(grayscale)
        enhanced_output = os.path.join(OUTPUT_FOLDER, f'{output_prefix}_enhanced.png')
        cv2.imwrite(enhanced_output, enhanced)
        
        # Apply Gaussian Blur
        blurred = cv2.GaussianBlur(enhanced, (5, 5), 1)
        blurred_output = os.path.join(OUTPUT_FOLDER, f'{output_prefix}_blurred.png')
        cv2.imwrite(blurred_output, blurred)
        
        # Apply Canny Edge Detection
        edges = cv2.Canny(blurred, 100, 200)
        edges_output = os.path.join(OUTPUT_FOLDER, f'{output_prefix}_edges.png')
        cv2.imwrite(edges_output, edges)
        
        # Return paths relative to static folder for web display
        return {
            'original': f'/static/outputs/{output_prefix}_original.png',
            'grayscale': f'/static/outputs/{output_prefix}_grayscale.png',
            'enhanced': f'/static/outputs/{output_prefix}_enhanced.png',
            'blurred': f'/static/outputs/{output_prefix}_blurred.png',
            'edges': f'/static/outputs/{output_prefix}_edges.png',
            'success': True
        }
    except Exception as e:
        import traceback
        return {
            'success': False,
            'error': str(e)
        }


def create_zip_download(output_prefix):
    """
    Create a ZIP file containing all processed images.
    
    Args:
        output_prefix (str): Prefix of the processed images
        
    Returns:
        str: Path to the created ZIP file
    """
    zip_path = os.path.join(OUTPUT_FOLDER, f'{output_prefix}_results.zip')
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add all processed images to the ZIP file
        for image_type in ['original', 'grayscale', 'enhanced', 'blurred', 'edges']:
            image_path = os.path.join(OUTPUT_FOLDER, f'{output_prefix}_{image_type}.png')
            if os.path.exists(image_path):
                # Archive name will be just the filename (no folder structure)
                zipf.write(image_path, arcname=f'{output_prefix}_{image_type}.png')
    
    return zip_path


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload and image processing.
    Creates a unique prefix based on timestamp for each upload.
    """
    # Check if file is present in request
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    # Check if file is selected
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400
    
    # Check if file is allowed
    if not allowed_file(file.filename):
        return jsonify({'success': False, 'error': 'Invalid file type. Please upload JPG or PNG.'}), 400
    
    try:
        # Create unique output prefix using timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_prefix = f'medical_{timestamp}'
        
        # Get original file extension
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        
        # Save uploaded file temporarily with original extension
        uploaded_path = os.path.join(UPLOAD_FOLDER, f'{output_prefix}_temp.{file_ext}')
        file.save(uploaded_path)
        
        # Verify file was saved
        if not os.path.exists(uploaded_path):
            return jsonify({'success': False, 'error': 'Failed to save uploaded file'}), 500
        
        # Verify file has content
        if os.path.getsize(uploaded_path) == 0:
            return jsonify({'success': False, 'error': 'Uploaded file is empty'}), 400
        
        # Process the image
        result = process_medical_image(uploaded_path, output_prefix)
        
        if not result['success']:
            return jsonify(result), 400
        
        # Add output prefix to result for ZIP download
        result['output_prefix'] = output_prefix
        
        # Clean up temporary file
        try:
            os.remove(uploaded_path)
        except:
            pass
        
        return jsonify(result), 200
    
    except Exception as e:
        import traceback
        error_msg = f"{str(e)} - {traceback.format_exc()}"
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/download/<output_prefix>')
def download_results(output_prefix):
    """Download all processed images as a ZIP file."""
    try:
        # Validate output_prefix to prevent directory traversal
        if '..' in output_prefix or '/' in output_prefix:
            return jsonify({'error': 'Invalid request'}), 400
        
        zip_path = create_zip_download(output_prefix)
        
        return send_file(
            zip_path,
            as_attachment=True,
            download_name=f'{output_prefix}_results.zip',
            mimetype='application/zip'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error."""
    return jsonify({'success': False, 'error': 'File is too large (max 20MB)'}), 413


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Run Flask development server
    # Set debug=True for development, debug=False for production
    app.run(debug=True, host='0.0.0.0', port=5000)
