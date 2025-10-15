import pdfplumber
import re

def parse_credit_card_statement(pdf_path):
    """Extract key information from credit card statement"""
    
    with pdfplumber.open(pdf_path) as pdf:
        # Get all text from PDF
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    
    # Detect bank
    text_upper = text.upper()
    if 'AXIS BANK' in text_upper:
        bank = 'AXIS'
    elif 'HDFC BANK' in text_upper:
        bank = 'HDFC'
    elif 'ICICI BANK' in text_upper:
        bank = 'ICICI'
    elif 'KOTAK' in text_upper:
        bank = 'KOTAK'
    elif 'SBI' in text_upper:
        bank = 'SBI'
    else:
        bank = 'UNKNOWN'
    
    # Extract card number
    card_match = re.search(r'XXXX\s+XXXX\s+XXXX\s+(\d{4})', text)
    card_number = f"****{card_match.group(1)}" if card_match else "Not Found"
    
    # Extract statement date
    stmt_date_match = re.search(r'Statement Date[:\s]+(\d{1,2}-\w{3}-\d{4})', text, re.I)
    statement_date = stmt_date_match.group(1) if stmt_date_match else "Not Found"
    
    # Extract total due - handles 'n' character and newlines
    # Pattern: "Total Amount Due:" followed by newlines, then "n 70,487"
    total_due_match = re.search(r'Total Amount Due:.*?[n₹■]?\s*([\d,]+)', text, re.I | re.DOTALL)
    total_due = f"₹{total_due_match.group(1)}" if total_due_match else "Not Found"
    
    # Extract due date - handles newlines between label and value
    due_date_match = re.search(r'Payment Due Date:.*?(\d{1,2}-\w{3}-\d{4})', text, re.I | re.DOTALL)
    due_date = due_date_match.group(1) if due_date_match else "Not Found"
    
    # Extract credit limit - handles 'n' character
    credit_limit_match = re.search(r'Credit Limit:\s*[n₹■]?\s*([\d,]+)', text, re.I)
    credit_limit = f"₹{credit_limit_match.group(1)}" if credit_limit_match else "Not Found"
    
    return {
        'bank': bank,
        'card_number': card_number,
        'statement_date': statement_date,
        'total_due': total_due,
        'due_date': due_date,
        'credit_limit': credit_limit
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        result = parse_credit_card_statement(sys.argv[1])
        for key, value in result.items():
            print(f"{key}: {value}")