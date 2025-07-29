import qrcode

# Data to encode
data = "https://example.com"

# Create QR Code instance
qr = qrcode.QRCode(
    version=1,  # controls size of QR Code (1 to 40)
    box_size=10,  # size of each box in pixels
    border=4     # thickness of the border (default 4)
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qr_code.png")

print("✅ QR code generated and saved as my_qr_code.png")
