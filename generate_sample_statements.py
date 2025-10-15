from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime, timedelta
import random
import os

class IndianBankStatementGenerator:
    """Generate realistic Indian credit card statements"""
    
    def __init__(self):
        self.banks = {
            'HDFC': {
                'name': 'HDFC Bank Ltd.',
                'color': colors.HexColor('#ED232A'),
                'address': 'HDFC Bank House, Senapati Bapat Marg, Lower Parel, Mumbai - 400013',
                'card_prefix': 'HDFC'
            },
            'ICICI': {
                'name': 'ICICI Bank Limited',
                'color': colors.HexColor('#F36F21'),
                'address': 'ICICI Bank Towers, Bandra Kurla Complex, Mumbai - 400051',
                'card_prefix': 'ICICI'
            },
            'SBI': {
                'name': 'SBI Card',
                'color': colors.HexColor('#22409A'),
                'address': 'DLF Infinity Towers, DLF Cyber City, Gurgaon - 122002',
                'card_prefix': 'SBI'
            },
            'AXIS': {
                'name': 'Axis Bank Ltd.',
                'color': colors.HexColor('#97144D'),
                'address': 'Axis House, C-2, Wadia International Centre, Mumbai - 400025',
                'card_prefix': 'AXIS'
            },
            'KOTAK': {
                'name': 'Kotak Mahindra Bank',
                'color': colors.HexColor('#ED1C24'),
                'address': '27 BKC, Bandra Kurla Complex, Mumbai - 400051',
                'card_prefix': 'KOTAK'
            }
        }
    
    def create_statement(self, bank_code, cardholder_name, last_4_digits, file_name):
        """Create a credit card statement for a specific bank"""
        
        # Define the directory path
        output_dir = r'uploads'
        
        # Create the full file path
        file_path = os.path.join(output_dir, file_name)
        
        bank = self.banks[bank_code]
        c = canvas.Canvas(file_path, pagesize=A4)
        width, height = A4
        
        # Calculate dates
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        due_date = end_date + timedelta(days=20)
        
        # Generate random amounts
        total_due = random.randint(15000, 85000)
        credit_limit = random.choice([100000, 150000, 200000, 250000, 300000, 500000])
        min_payment = int(total_due * 0.05)
        
        # --- Header ---
        c.setFillColor(bank['color'])
        c.rect(0, height - 1.5*inch, width, 1.5*inch, stroke=0, fill=1)
        
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(0.5*inch, height - 0.8*inch, bank['name'])
        
        c.setFont("Helvetica", 9)
        c.drawString(0.5*inch, height - 1.1*inch, bank['address'])
        
        # --- Watermark ---
        c.saveState()
        c.setFont("Helvetica-Bold", 60)
        c.setFillColor(colors.Color(0.9, 0.9, 0.9, alpha=0.3))
        c.rotate(45)
        c.drawString(2*inch, 0.5*inch, "SAMPLE STATEMENT")
        c.restoreState()
        
        # --- Statement Header ---
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(0.5*inch, height - 2*inch, "CREDIT CARD STATEMENT")
        
        # --- Cardholder Details ---
        y_pos = height - 2.5*inch
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.5*inch, y_pos, "Cardholder Name:")
        c.setFont("Helvetica", 11)
        c.drawString(2*inch, y_pos, cardholder_name.upper())
        
        y_pos -= 0.25*inch
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.5*inch, y_pos, "Card Number:")
        c.setFont("Helvetica", 11)
        c.drawString(2*inch, y_pos, f"XXXX XXXX XXXX {last_4_digits}")
        
        # --- Statement Period ---
        y_pos -= 0.25*inch
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.5*inch, y_pos, "Statement Date:")
        c.setFont("Helvetica", 11)
        c.drawString(2*inch, y_pos, end_date.strftime('%d-%b-%Y'))
        
        y_pos -= 0.25*inch
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.5*inch, y_pos, "Billing Cycle:")
        c.setFont("Helvetica", 11)
        c.drawString(2*inch, y_pos, f"{start_date.strftime('%d-%b-%Y')} to {end_date.strftime('%d-%b-%Y')}")
        
        # --- Payment Details Box (Right Side) ---
        box_x = width - 3.5*inch
        box_y = height - 3.2*inch
        box_width = 3*inch
        box_height = 1.8*inch
        
        # Red border box
        c.setStrokeColor(colors.red)
        c.setLineWidth(2)
        c.rect(box_x, box_y, box_width, box_height, stroke=1, fill=0)
        
        # Payment details inside box
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.red)
        c.drawString(box_x + 0.2*inch, box_y + box_height - 0.35*inch, "Payment Due Date:")
        c.setFont("Helvetica-Bold", 11)
        c.drawString(box_x + 0.2*inch, box_y + box_height - 0.6*inch, due_date.strftime('%d-%b-%Y'))
        
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(colors.black)
        c.drawString(box_x + 0.2*inch, box_y + box_height - 1*inch, "Total Amount Due:")
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.red)
        c.drawString(box_x + 0.2*inch, box_y + box_height - 1.3*inch, f"₹ {total_due:,}")
        
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.black)
        c.drawString(box_x + 0.2*inch, box_y + box_height - 1.6*inch, f"Minimum Payment: ₹ {min_payment:,}")
        
        # --- Credit Limit ---
        y_pos -= 0.25*inch
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.5*inch, y_pos, "Credit Limit:")
        c.setFont("Helvetica", 11)
        c.drawString(2*inch, y_pos, f"₹ {credit_limit:,}")
        
        y_pos -= 0.25*inch
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.5*inch, y_pos, "Available Credit:")
        c.setFont("Helvetica", 11)
        available = credit_limit - total_due
        c.drawString(2*inch, y_pos, f"₹ {available:,}")
        
        # --- Transaction History ---
        y_pos -= 0.6*inch
        c.setFont("Helvetica-Bold", 14)
        c.drawString(0.5*inch, y_pos, "Transaction Details")
        
        # Table header
        y_pos -= 0.3*inch
        c.setFillColor(colors.HexColor('#F0F0F0'))
        c.rect(0.5*inch, y_pos - 0.05*inch, width - 1*inch, 0.25*inch, stroke=0, fill=1)
        
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0.6*inch, y_pos, "Date")
        c.drawString(2*inch, y_pos, "Description")
        c.drawRightString(width - 0.6*inch, y_pos, "Amount (₹)")
        
        # Sample transactions
        merchants = [
            "AMAZON.IN", "SWIGGY", "FLIPKART", "ZOMATO", "UBER INDIA",
            "BIG BAZAAR", "DMart", "RELIANCE DIGITAL", "BOOKMYSHOW",
            "MAKEMYTRIP", "OYO ROOMS", "NETFLIX INDIA", "SPOTIFY"
        ]
        
        transactions = []
        running_total = 0
        for i in range(8):
            trans_date = end_date - timedelta(days=random.randint(2, 28))
            merchant = random.choice(merchants)
            amount = random.randint(500, 15000)
            transactions.append((trans_date, merchant, amount))
            running_total += amount
        
        # Adjust last transaction to match total
        transactions[-1] = (transactions[-1][0], transactions[-1][1], 
                           total_due - running_total + transactions[-1][2])
        
        # Sort by date
        transactions.sort(key=lambda x: x[0])
        
        c.setFont("Helvetica", 9)
        y_pos -= 0.3*inch
        
        for trans_date, merchant, amount in transactions:
            c.drawString(0.6*inch, y_pos, trans_date.strftime('%d-%b-%Y'))
            c.drawString(2*inch, y_pos, merchant)
            c.drawRightString(width - 0.6*inch, y_pos, f"{amount:,}.00")
            y_pos -= 0.25*inch
            if y_pos < 2*inch:  # Leave space for footer
                break
        
        # --- Summary Line ---
        y_pos -= 0.2*inch
        c.setStrokeColor(colors.black)
        c.line(0.5*inch, y_pos, width - 0.5*inch, y_pos)
        
        y_pos -= 0.25*inch
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.6*inch, y_pos, "Total Transactions:")
        c.drawRightString(width - 0.6*inch, y_pos, f"₹ {total_due:,}")
        
        # --- Footer ---
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColor(colors.grey)
        footer_y = 1*inch
        c.drawString(0.5*inch, footer_y, "This is a sample statement for demonstration purposes only.")
        c.drawString(0.5*inch, footer_y - 0.15*inch, 
                    f"{bank['name']} | Customer Care: 1800-XXX-XXXX | www.{bank_code.lower()}bank.com")
        c.drawString(0.5*inch, footer_y - 0.3*inch, 
                    "For any queries, please contact our 24x7 customer support.")
        
        # Save
        c.save()
        print(f"✓ Created: {file_path}")
    
    def generate_all_statements(self):
        """Generate statements for all 5 banks"""
        
        cardholders = [
            ("Rajesh Kumar", "4589"),
            ("Priya Sharma", "7823"),
            ("Amit Patel", "3456"),
            ("Sneha Reddy", "9012"),
            ("Vikram Singh", "6789")
        ]
        
        print("\n Generating Indian Bank Credit Card Statements...\n")
        
        for i, (bank_code, bank_info) in enumerate(self.banks.items()):
            name, last_4 = cardholders[i]
            filename = f"{bank_code}_Statement_{last_4}.pdf"
            self.create_statement(bank_code, name, last_4, filename)
        
        print("\nAll 5 bank statements created successfully!")
        print("\nFiles created:")
        for bank_code in self.banks.keys():
            print(f"  • {bank_code}_Statement_*.pdf")

# Run the generator
if __name__ == "__main__":
    generator = IndianBankStatementGenerator()
    generator.generate_all_statements()
