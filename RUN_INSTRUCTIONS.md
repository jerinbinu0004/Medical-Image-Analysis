# 🏥 How to Run Medical Image Processing System

Complete step-by-step guide to get the application running.

## Quick Start (5 minutes)

### Step 1: Install Dependencies
```bash
cd /workspaces/Medical-Image-Analysis
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
```
http://localhost:5000
```

---

## Detailed Setup Instructions

### Prerequisites
- **Python 3.8 or higher** installed
- **pip** (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Verify Python Installation
```bash
python3 --version
```
Should show version 3.8 or higher.

---

## Windows Users

### Step 1: Open Command Prompt or PowerShell
- Press `Win + R`
- Type `cmd` or `powershell`
- Press Enter

### Step 2: Navigate to Project Directory
```bash
cd C:\path\to\Medical-Image-Analysis
```

### Step 3: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the Application
```bash
python app.py
```

### Step 6: Open Browser
- Type in address bar: `http://localhost:5000`
- Press Enter

---

## Mac/Linux Users

### Step 1: Open Terminal
- Mac: Cmd + Space, type "Terminal"
- Linux: Ctrl + Alt + T

### Step 2: Navigate to Project Directory
```bash
cd /path/to/Medical-Image-Analysis
```

### Step 3: Create Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the Application
```bash
python app.py
```

### Step 6: Open Browser
- Open your browser
- Go to: `http://localhost:5000`

---

## Using the Application

### 1. Upload an X-ray Image
![Upload Section]
- Click **"📁 Choose X-ray Image"** button
- Select a JPG or PNG file from your computer
- **OR** drag and drop an image onto the upload area

### 2. Click Process Button
- Click **"📤 Process Image"** button
- Wait for processing (2-5 seconds)
- Loading spinner will show progress

### 3. View Results
Five processed images will appear:
- **Original Image** - Your uploaded image
- **Grayscale** - Converted to black & white
- **Enhanced** - Contrast improved
- **Blurred** - Smoothed version
- **Edges** - Edge detection result

### 4. Download Results
- Click **"📦 Download Results (ZIP)"** button
- All 5 images will download as a ZIP file

### 5. Process Another Image
- Click **"🔄 Reset"** to start over
- Upload a new image

---

## Full Setup with Virtual Environment (Recommended)

This is the safest way to run the application:

### Windows
```bash
# Navigate to project
cd C:\Users\YourName\Medical-Image-Analysis

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

### Mac/Linux
```bash
# Navigate to project
cd ~/Medical-Image-Analysis

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application  
python app.py
```

### Expected Output
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
Debugger PIN: 123-456-789
```

---

## Checklist Before Running

- [ ] Python 3.8+ installed
- [ ] You're in the correct directory (`Medical-Image-Analysis`)
- [ ] Requirements installed (`pip install -r requirements.txt`)
- [ ] Port 5000 is available
- [ ] You have a JPG or PNG image to test with

---

## Troubleshooting

### ❌ "Python not found"
```bash
# Use python3 instead
python3 app.py
```

### ❌ "ModuleNotFoundError: No module named 'flask'"
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### ❌ "Port 5000 already in use"
This means another application is using port 5000.

**Option 1:** Kill the process using port 5000
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :5000
kill -9 <PID>
```

**Option 2:** Use a different port
```bash
python -c "from app import app; app.run(port=5001)"
```
Then open: `http://localhost:5001`

### ❌ "Unexpected end of JSON input" error in browser
This means the Flask server isn't running properly.

**Solution:**
```bash
# 1. Kill any existing Flask process
pkill -f "python app.py"

# 2. Reinstall dependencies
pip install -r requirements.txt --upgrade

# 3. Start Flask again
python app.py
```

### ❌ "Image processing failed"
- Make sure the image is a valid JPG or PNG
- Image should be less than 20MB
- Try with a smaller image

### ❌ Cannot access http://localhost:5000
- Verify Flask is running (you should see the server output)
- Try a different browser
- Check if port 5000 is being blocked by firewall
- Try `http://127.0.0.1:5000` instead

---

## File Upload Tips

### Recommended Image Specifications
- **Format:** JPG or PNG
- **Size:** 500px - 2000px wide (smaller = faster)
- **File Size:** Under 10MB
- **Type:** Medical X-rays work best

### Test Images
- Use any JPG or PNG X-ray image
- If you don't have one, download a sample from:
  - Google Images (search "X-ray medical")
  - Medical image databases

---

## Stopping the Application

### Windows
- Press `Ctrl + C` in the command prompt
- Confirm with `Y` if prompted

### Mac/Linux
- Press `Ctrl + C` in the terminal
- Press again if needed

---

## Deactivating Virtual Environment (Optional)

When you're done:
```bash
# All operating systems
deactivate
```

---

## Running in the Background (Advanced)

### Windows
```bash
# Start Flask using pythonw (no console window)
pythonw app.py
```

### Mac/Linux
```bash
# Start Flask in background
python app.py &

# To stop it later
pkill -f "python app.py"
```

---

## Testing the Application

A test script is included. Run it to verify everything works:

```bash
python test_app.py
```

You should see:
```
✓ Homepage loaded successfully
✓ JSON response received successfully
✓ Image processing successful!
```

---

## Production Deployment (Advanced)

For hosting on a server, use Gunicorn instead of Flask's debug server:

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## Need Help?

If you encounter issues:

1. **Check the error message** - Read what it says carefully
2. **Check requirements** - Ensure all dependencies are installed
3. **Restart Flask** - Stop (Ctrl+C) and run `python app.py` again
4. **Check port** - Ensure port 5000 is free
5. **Clear browser cache** - Might be showing cached error
6. **Try different browser** - Verify it's not a browser issue

---

## Quick Reference Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Upgrade dependencies
pip install -r requirements.txt --upgrade

# Run application
python app.py

# Run with different port
python -c "from app import app; app.run(port=5001)"

# Test application
python test_app.py

# Find process using port 5000
lsof -i :5000  # Mac/Linux
netstat -ano | findstr :5000  # Windows

# Kill process
kill -9 <PID>  # Mac/Linux
taskkill /PID <PID> /F  # Windows
```

---

**Last Updated:** February 2026  
**Version:** 1.0  
**Status:** ✅ Fully Functional
