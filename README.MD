Credit Card Statement Parser

A web application that automatically extracts key information from credit card statements with a built-in PDF generator for testing.

Project Overview

Developed as a technical assignment for Sure Technologies, this project demonstrates a complete data extraction solution from test data generation to deployment.

Two main components:

1. PDF Generation Script
   - Uses ReportLab to create bank-specific statements
   - Includes realistic branding, transactions, and formatting
   
2. Web Parsing Application
   - Extracts data using pdfplumber and regex
   - Auto-detects banks and handles errors

Core Functionality

- Generates sample statements for five major Indian banks
- Extracts six critical data points from uploaded PDFs
- Provides drag-and-drop web interface
- Automatically identifies issuing bank
- Displays results instantly

Supported Banks and Extracted Data

Banks: HDFC, ICICI, SBI Card, Axis, Kotak Mahindra

Extracted Information:
1. Bank Name
2. Card Number (last 4 digits)
3. Statement Date
4. Total Amount Due
5. Payment Due Date
6. Credit Limit

Technology Stack

Backend: Python 3.8+, Flask, pdfplumber, Regular Expressions, ReportLab
Frontend: HTML5, CSS3, Vanilla JavaScript

Installation and Usage

Prerequisites: Python 3.8+, pip

Quick Start:
1. Navigate to project directory
2. Install dependencies: pip install -r requirements.txt
3. Generate samples (optional): python generate_sample_statements.py
4. Start server: python app.py
5. Visit: http://127.0.0.1:5000

Application Usage:
Upload PDF via drag-and-drop or click, then click Parse Statement to view extracted data in table format.

Project Structure

credit-card-parser/
├── app.py                          # Flask server
├── parser.py                       # Extraction logic
├── generate_sample_statements.py   # PDF generator
├── requirements.txt                # Dependencies
├── templates/
│   └── index.html                  # UI
└── uploads/                        # PDF storage

Technical Implementation

PDF Generation:
Creates realistic statements with bank branding, random transactions (15,000-85,000 rupees), and credit limits (100,000-500,000 rupees) using predefined merchant lists.

PDF Parsing:
Four-step process: extract text with pdfplumber, detect bank via keywords, match patterns with regex, format output. Handles currency symbol variations and multi-line patterns using DOTALL flag.

Challenges and Solutions

1. Currency Symbol Issue
   Rupee symbol extracted as 'n' - solved by matching both characters in regex.

2. Multi-line Patterns
   Data spans multiple lines - solved with DOTALL flag and non-greedy matching.

3. Bank Variations
   Different formatting across banks - solved with flexible regex patterns.

Limitations and Future Improvements

Current Limits:
- Five banks only
- Standard formatting required
- No OCR for scanned PDFs
- Six data points only

Future Enhancements:
- More bank support
- OCR implementation
- Additional data extraction
- Export to CSV/JSON
- Batch processing

Testing

Quick test options:
1. Generate samples: python generate_sample_statements.py
2. Command line test: python parser.py uploads/KOTAK_Statement_6789.pdf
3. Web interface: Upload generated PDFs

Error Handling

Handles invalid file types, 16MB size limit, corrupted PDFs, and missing data. Provides clear error messages for all issues.

Security Considerations

Implements secure_filename for sanitization, 16MB upload limit, PDF-only restriction, and temporary file storage with optional auto-cleanup.

Dependencies

Flask 3.0.0, pdfplumber 0.10.3, Werkzeug 3.0.1, reportlab 4.0.0
Install via: pip install -r requirements.txt

Author and Purpose

Technical assignment for Sure Technologies demonstrating full-stack development, PDF parsing, problem-solving, and clean code practices.

License

Educational and demonstration purposes only.

