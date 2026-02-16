#!/bin/bash
# Quick setup and run script for Medical Image Processing System

echo "🏥 Medical Image Processing System - Setup Guide"
echo "=================================================="
echo ""

# Step 1: Check Python version
echo "Step 1: Checking Python version..."
python3 --version || { echo "❌ Python 3 not installed"; exit 1; }

# Step 2: Create virtual environment
echo ""
echo "Step 2: Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Step 3: Activate virtual environment
echo ""
echo "Step 3: Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

# Step 4: Install dependencies
echo ""
echo "Step 4: Installing dependencies..."
echo "This may take a few minutes on first run..."
pip install -r requirements.txt > /dev/null 2>&1
echo "✓ Dependencies installed"

# Step 5: Display startup information
echo ""
echo "=================================================="
echo "✓ Setup Complete!"
echo "=================================================="
echo ""
echo "To start the Flask application, run:"
echo "  source venv/bin/activate  (if not already activated)"
echo "  python app.py"
echo ""
echo "Then open your browser to:"
echo "  http://localhost:5000"
echo ""
echo "=================================================="
