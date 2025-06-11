# Construction Submission Extractor

This simple Python application provides a graphical interface for extracting
key information from construction submission documents. It supports both text
files and PDF files.

## Features
- Select a submission file (`.txt` or `.pdf`) through the GUI.
- Automatically extracts lines containing keywords such as `Project Name`,
  `Budget`, `Start Date`, `End Date`, and `Client`.
- Displays the extracted information in the application window.

## Usage
1. Install dependencies:
   ```bash
   pip install PyPDF2
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Click **"Select Submission File"** to choose the document you want to
   analyze.

The application will show any detected fields in the output area.

## EXE Builder

This repository also includes a simple GUI tool for packaging Python scripts
into standalone Windows executables using PyInstaller.

### Usage

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Run the builder:
   ```bash
   python builder.py
   ```
3. Choose the Python script you want to package and configure any desired
   options. Click **Build** to generate the executable in the selected output
   directory.
