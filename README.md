# Medical Image Processing System

A simple yet powerful Flask web application for processing X-ray images with various advanced image processing techniques. Upload an X-ray image and apply multiple processing filters to enhance and analyze the medical imagery.

## Features

- **Image Upload**: Upload JPG or PNG X-ray images (up to 20MB)
- **Grayscale Conversion**: Convert color images to grayscale for standardized analysis
- **Histogram Equalization**: Enhance contrast to reveal more details in the image
- **Gaussian Blur**: Smooth the image to reduce noise
- **Canny Edge Detection**: Detect edges to identify boundaries and structures
- **Batch Processing**: All processed images are saved automatically
- **ZIP Download**: Download all results as a single ZIP file
- **Responsive UI**: Clean, modern interface that works on desktop and mobile
- **Real-time Processing**: Fast image processing with visual feedback

## Project Structure

```
Medical-Image-Analysis/
├── app.py                      # Flask application and image processing logic
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/
│   └── index.html             # HTML template with CSS and JavaScript
├── static/
│   ├── uploads/               # Temporary storage for uploaded images
│   └── outputs/               # Processed images and ZIP files
└── outputs/                   # Output folder for final results
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone or Navigate to the Project

```bash
cd Medical-Image-Analysis
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **Flask**: Web framework
- **opencv-python-headless**: Computer vision library for image processing
- **numpy**: Numerical computing library
- **Werkzeug**: WSGI utility library

## Running the Application

### Start the Flask Server

```bash
python app.py
```

You should see output like:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

### Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

The Medical Image Processing System interface should load.

## Usage Guide

### Step 1: Upload an Image

1. Click the **"📁 Choose X-ray Image"** button
2. Select a JPG or PNG file from your computer
3. Or drag and drop an image directly onto the upload area

### Step 2: Submit for Processing

1. After selecting an image, click the **"📤 Process Image"** button
2. Wait for the processing to complete (usually 2-5 seconds)
3. A loading spinner will show progress

### Step 3: View Results

After processing completes, you'll see all five processed images:

- **Original Image**: The uploaded image in its original state
- **Grayscale**: Converted to grayscale (no color information)
- **Enhanced**: Histogram equalization applied for better contrast
- **Blurred**: Gaussian blur applied to smooth the image
- **Canny Edge Detection**: Edges detected in the image

### Step 4: Download Results

Click the **"📦 Download Results (ZIP)"** button to download all processed images as a single ZIP file.

### Step 5: Process Another Image

Click the **"🔄 Reset"** button to clear the current results and process a new image.

## Image Processing Techniques Explained

### Grayscale Conversion
Converts RGB (color) images to grayscale by removing color information. Useful for:
- Standardized medical image analysis
- Reducing file size
- Preparing for advanced algorithms

### Histogram Equalization
Improves image contrast by redistributing pixel intensity values. Benefits:
- Reveals hidden details and structures
- Enhances visibility of lesions or abnormalities
- Better visualization for diagnosis

### Gaussian Blur
Applies a smoothing filter to reduce noise and detail. Purpose:
- Reduce image noise
- Smooth out minor artifacts
- Prepare for edge detection

### Canny Edge Detection
Identifies and highlights edges in the image. Useful for:
- Detecting boundaries of structures
- Identifying margins of lesions
- Structural analysis

## File Structure Details

### app.py

Main Flask application containing:
- **Route handlers**: HTTP endpoints for upload and download
- **Image processing functions**: Core image manipulation logic
- **ZIP creation**: Bundle all results for download
- **Error handling**: Comprehensive error management

### templates/index.html

Frontend interface providing:
- Responsive HTML structure
- Modern CSS styling with gradients and animations
- Drag-and-drop upload support
- Real-time feedback and loading indicators
- JavaScript for AJAX image upload

### Requirements

All Python dependencies needed for the application:
- Flask: Web server and routing
- opencv-python-headless: Image processing (headless version for servers)
- numpy: Numerical operations
- Werkzeug: Web utilities

## Configuration

Default configuration in `app.py`:

```python
UPLOAD_FOLDER = 'static/uploads'      # Temporary upload storage
OUTPUT_FOLDER = 'static/outputs'      # Processed images location
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}  # Allowed file types
MAX_FILE_SIZE = 20 * 1024 * 1024      # 20MB maximum file size
```

To change any setting, edit these variables in `app.py`.

## Troubleshooting

### Flask Server Won't Start

**Problem**: Port 5000 already in use
```bash
# Try a different port
python -c "from app import app; app.run(port=5001)"
```

### Module Not Found Errors

**Problem**: Dependencies not installed
```bash
# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Image Upload Fails

**Possible causes:**
- File format not supported (use JPG or PNG only)
- File size exceeds 20MB limit
- Browser cache issue (clear cache and try again)

### Processing Takes Too Long

**Note**: Processing time depends on:
- Image resolution
- Server CPU performance
- System load
- Typically takes 2-5 seconds

### "Unexpected end of JSON input" Error When Uploading

**Problem**: You see "Failed to execute 'json' on 'Response': Unexpected end of JSON input"

**Solution**: This error occurs when the Flask backend hasn't been started or dependencies aren't installed.

**Fix:**
```bash
# 1. Make sure you're in the correct directory
cd Medical-Image-Analysis

# 2. Activate virtual environment (if using one)
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# 3. Install/reinstall dependencies
pip install -r requirements.txt --upgrade

# 4. Verify Flask is working
python -c "import flask, cv2, numpy; print('✓ All modules installed')"

# 5. Start the Flask server
python app.py

# 6. Open browser to http://localhost:5000
```

**Common causes:**
- Flask server not running
- Dependencies not installed (Flask, OpenCV, numpy)
- Using an incompatible Python version (use 3.8+)
- Port 5000 in use by another application

### Results Not Displaying

**Troubleshooting:**
1. Check browser console for errors (F12)
2. Verify Flask server is running
3. Clear browser cache
4. Try a smaller image file

## Performance Tips

1. **Optimize Image Size**: Use images around 1024x1024 pixels for faster processing
2. **File Format**: PNG files may process slightly slower than JPG
3. **Server Resources**: Close other applications to free up resources
4. **Browser Cache**: Clear browser cache if images don't update

## Security Considerations

The application includes several security measures:

- **File Type Validation**: Only JPG and PNG files accepted
- **File Size Limit**: Maximum 20MB to prevent DOS attacks
- **Path Traversal Prevention**: Output prefix validation prevents malicious downloads
- **Error Handling**: Comprehensive error messages without exposing system details

## Browser Compatibility

Works with all modern browsers:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## System Requirements

### Minimum
- CPU: 2-core processor
- RAM: 2GB
- Disk: 500MB free space

### Recommended
- CPU: 4-core processor
- RAM: 4GB
- Disk: 1GB free space

## Deployment

For production deployment:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Set up a reverse proxy (Nginx, Apache)
4. Enable HTTPS/SSL certificates
5. Configure proper logging and monitoring

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## License

This project is provided as-is for educational and medical image analysis purposes.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit code enhancements

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the code comments
3. Check Flask and OpenCV documentation

## Disclaimer

This application is designed for educational purposes. For clinical use, always validate results with medical professionals and ensure compliance with relevant healthcare regulations and HIPAA requirements.

---

**Last Updated**: February 2026
**Version**: 1.0