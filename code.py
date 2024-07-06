import qrcode

# Example transaction data (replace with your actual data)
transaction_data = {
    'transaction_id': '123456789',
    'amount': '1000',
    'merchant_id': 'your_merchant_id',
    # Add any other relevant data here
}

# Create a string from transaction data (you can serialize it as JSON or concatenate fields)
data_string = f"Transaction ID: {transaction_data['transaction_id']}, Amount: {transaction_data['amount']}, Merchant ID: {transaction_data['merchant_id']}"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data_string)
qr.make(fit=True)

# Generate QR code image
qr_img = qr.make_image(fill='black', back_color='white')

# Save or display the QR code image
qr_img.save('transaction_qr.png')  # Save to file
# qr_img.show() 