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
