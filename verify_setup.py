#!/usr/bin/env python3
"""
🏥 QUICK START GUIDE - Medical Image Processing System
Run this script to verify everything is ready!
"""

import os
import sys
import subprocess

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def check_python():
    """Check Python version"""
    print("1️⃣  Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - OK\n")
        return True
    else:
        print(f"   ❌ Python 3.8+ required (found {version.major}.{version.minor})\n")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    print("2️⃣  Checking dependencies...")
    required = ['flask', 'cv2', 'numpy']
    all_ok = True
    
    for package in required:
        try:
            __import__(package)
            print(f"   ✅ {package} - installed")
        except ImportError:
            print(f"   ❌ {package} - NOT installed")
            all_ok = False
    
    if not all_ok:
        print(f"\n   📦 Run: pip install -r requirements.txt\n")
    else:
        print()
    
    return all_ok

def check_folders():
    """Check if required folders exist"""
    print("3️⃣  Checking folders...")
    required_folders = ['templates', 'static/uploads', 'static/outputs']
    all_ok = True
    
    for folder in required_folders:
        if os.path.isdir(folder):
            print(f"   ✅ {folder} - exists")
        else:
            print(f"   ❌ {folder} - missing")
            all_ok = False
    
    print()
    return all_ok

def check_files():
    """Check if required files exist"""
    print("4️⃣  Checking files...")
    required_files = ['app.py', 'requirements.txt', 'templates/index.html']
    all_ok = True
    
    for file in required_files:
        if os.path.isfile(file):
            print(f"   ✅ {file} - exists")
        else:
            print(f"   ❌ {file} - missing")
            all_ok = False
    
    print()
    return all_ok

def main():
    os.system('clear' if os.name != 'nt' else 'cls')
    
    print_header("🏥 Medical Image Processing System - Setup Check")
    
    # Run checks
    python_ok = check_python()
    deps_ok = check_dependencies()
    folders_ok = check_folders()
    files_ok = check_files()
    
    # Summary
    print_header("📋 Setup Summary")
    
    if python_ok and deps_ok and folders_ok and files_ok:
        print("✅ All checks passed! Ready to run!\n")
        print("📌 TO START THE APPLICATION:")
        print("   python app.py\n")
        print("🌐 Then open browser to:")
        print("   http://localhost:5000\n")
        return 0
    else:
        print("❌ Some issues found. Please fix before running:\n")
        
        if not python_ok:
            print("   • Update Python to 3.8 or higher")
        if not deps_ok:
            print("   • Run: pip install -r requirements.txt")
        if not folders_ok:
            print("   • Some folders are missing")
        if not files_ok:
            print("   • Some files are missing")
        
        print()
        return 1

if __name__ == '__main__':
    sys.exit(main())
