import os
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image

# Get user input for barcode data
data = input("Enter data to encode in barcode: ")

# Set directory where barcode image will be saved
output_dir = "generated_barcodes"
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

# Set filename for the barcode image
filename = os.path.join(output_dir, "barcode_output")

try:
    # Generate and save the barcode image
    barcode = Code128(data, writer=ImageWriter())
    barcode.save(filename)
    print(f"Barcode image saved as {filename}.png")
except Exception as e:
    print(f"Error saving barcode: {e}")