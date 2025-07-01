import qrcode
import json
from PIL import Image
from pyzbar.pyzbar import decode

# --- Step 1: Metadata Input ---
metadata = {
    "species": "Panthera tigris",
    "sample_id": "TGR001",
    "gene": "COI",
    "sequence": "ATGCGTACCGTATAGCCTAGG..."  # Truncated example
}

# --- Step 2: Convert metadata to JSON string ---
barcode_data = json.dumps(metadata)

# --- Step 3: Generate QR code ---
qr = qrcode.make(barcode_data)
qr.save("dna_barcode.png")
print("✅ QR code generated and saved as dna_barcode.png")

# --- Step 4 (Optional): Decode QR code and extract metadata ---
def decode_qr_code(image_path):
    img = Image.open(image_path)
    result = decode(img)
    if result:
        data = result[0].data.decode("utf-8")
        decoded_metadata = json.loads(data)
        print("🔍 Decoded Data:", decoded_metadata)
    else:
        print("⚠️ No QR code found in image.")

# Uncomment to test decoding
# decode_qr_code("dna_barcode.png")