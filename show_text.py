import pdfplumber
import sys
import os

# Check if file provided
if len(sys.argv) < 2:
    print("Usage: python show_text.py <pdf_file>")
    print("\nTrying default: uploads/KOTAK_Statement_6789.pdf")
    pdf_path = "uploads/KOTAK_Statement_6789.pdf"
else:
    pdf_path = sys.argv[1]

# Check if file exists
if not os.path.exists(pdf_path):
    print(f"\nERROR: File not found: {pdf_path}")
    print("\nLooking for PDF files in current directory and uploads/...")
    
    # Check current directory
    for f in os.listdir('.'):
        if f.endswith('.pdf'):
            print(f"  Found: {f}")
    
    # Check uploads directory
    if os.path.exists('uploads'):
        for f in os.listdir('uploads'):
            if f.endswith('.pdf'):
                print(f"  Found: uploads/{f}")
    
    sys.exit(1)

print(f"\n{'='*80}")
print(f"Reading: {pdf_path}")
print(f"{'='*80}\n")

try:
    with pdfplumber.open(pdf_path) as pdf:
        print(f"PDF has {len(pdf.pages)} page(s)")
        
        # Extract text from first page
        page = pdf.pages[0]
        text = page.extract_text()
        
        if not text:
            print("\nERROR: No text extracted from PDF!")
            print("The PDF might be image-based or corrupted.")
            sys.exit(1)
        
        print("\n" + "="*80)
        print("RAW TEXT FROM PDF:")
        print("="*80)
        print(text)
        print("="*80)
        
        # Now search for our fields
        import re
        
        print("\n\nSEARCHING FOR KEY FIELDS:\n")
        
        # 1. Total Amount Due
        print("1. Total Amount Due:")
        if 'Total Amount Due' in text:
            print("   ✓ FOUND")
            idx = text.index('Total Amount Due')
            snippet = text[idx:idx+150]
            print(f"   Context: {snippet}")
            print(f"   Repr: {repr(snippet)}")
        else:
            print("   ✗ NOT FOUND")
        
        # 2. Credit Limit
        print("\n2. Credit Limit:")
        if 'Credit Limit' in text:
            print("   ✓ FOUND")
            idx = text.index('Credit Limit')
            snippet = text[idx:idx+100]
            print(f"   Context: {snippet}")
            print(f"   Repr: {repr(snippet)}")
        else:
            print("   ✗ NOT FOUND")
        
        # 3. Payment Due Date
        print("\n3. Payment Due Date:")
        if 'Payment Due Date' in text:
            print("   ✓ FOUND")
            idx = text.index('Payment Due Date')
            snippet = text[idx:idx+100]
            print(f"   Context: {snippet}")
            print(f"   Repr: {repr(snippet)}")
        else:
            print("   ✗ NOT FOUND")
        
        # 4. Find all comma-separated numbers
        print("\n4. All numbers with commas:")
        amounts = re.findall(r'[\d,]{5,}', text)
        print(f"   {amounts[:20]}")  # First 20 matches
        
        print("\n" + "="*80)
        print("DONE")
        print("="*80)

except Exception as e:
    print(f"\nERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()