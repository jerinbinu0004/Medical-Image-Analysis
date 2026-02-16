#!/usr/bin/env python3
"""
Simple test script to verify the Flask app is working correctly.
"""

import requests
import json
import time
import sys

# Start the server first
print("Testing Medical Image Processing System...")
print("=" * 50)

# Test the homepage
try:
    response = requests.get('http://localhost:5000/', timeout=5)
    if response.status_code == 200:
        print("✓ Homepage loaded successfully")
    else:
        print(f"✗ Homepage returned status: {response.status_code}")
except Exception as e:
    print(f"✗ Could not connect to Flask server: {e}")
    sys.exit(1)

# Test image upload
print("\nTesting image upload...")
try:
    with open('xray.jpg', 'rb') as f:
        files = {'file': f}
        response = requests.post('http://localhost:5000/upload', files=files, timeout=30)
        
    print(f"Response status: {response.status_code}")
    print(f"Response headers: {response.headers}")
    print(f"Response content type: {response.headers.get('content-type')}")
    print(f"Response length: {len(response.text)} bytes")
    
    if response.status_code == 200:
        data = response.json()
        print("✓ JSON response received successfully")
        print(f"Response data: {json.dumps(data, indent=2)}")
        
        if data.get('success'):
            print("✓ Image processing successful!")
        else:
            print(f"✗ Processing failed: {data.get('error')}")
    else:
        print(f"✗ Upload failed with status {response.status_code}")
        print(f"Response: {response.text[:500]}")
        
except json.JSONDecodeError as e:
    print(f"✗ JSON decode error: {e}")
    print(f"Response text: {response.text[:500]}")
except Exception as e:
    print(f"✗ Error: {e}")

print("\nTest complete!")
