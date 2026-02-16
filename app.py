"""
Medical Image Processing Web Application
Updated Version - Uses medical_image_project.py for processing
"""

from flask import Flask, render_template, request, send_file, jsonify
import os
from datetime import datetime
import zipfile

# Import processing function from external file
from medical_image_project import process_image

# Initialize Flask app (explicit folders for static/templates)
app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

# Configuration
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB

# Create required directories
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'success': False, 'error': 'Invalid file type. Upload JPG or PNG.'}), 400

    try:
        # Unique prefix
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_prefix = f'medical_{timestamp}'

        file_ext = file.filename.rsplit('.', 1)[1].lower()
        uploaded_path = os.path.join(UPLOAD_FOLDER, f'{output_prefix}.{file_ext}')

        file.save(uploaded_path)

        # Process image using medical_image_project.py
        processed_images = process_image(uploaded_path)

        if processed_images is None:
            return jsonify({'success': False, 'error': 'Image processing failed'}), 400

        return jsonify({
            'success': True,
            'output_prefix': output_prefix,
            'images': [f'/static/{img}' for img in processed_images]
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/download/<output_prefix>')
def download_results(output_prefix):

    try:
        if '..' in output_prefix or '/' in output_prefix:
            return jsonify({'error': 'Invalid request'}), 400

        zip_path = os.path.join(OUTPUT_FOLDER, f'{output_prefix}_results.zip')

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in os.listdir(OUTPUT_FOLDER):
                if file.endswith('.jpg') or file.endswith('.png'):
                    full_path = os.path.join(OUTPUT_FOLDER, file)
                    zipf.write(full_path, arcname=file)

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
    return jsonify({'success': False, 'error': 'File too large (max 20MB)'}), 413


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Bind to 0.0.0.0 so the server is reachable from the host
    app.run(host='0.0.0.0', port=5000, debug=True)
