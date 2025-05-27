from cryptography.fernet import Fernet
from PIL import Image
from pyzbar.pyzbar import decode
import os
from pdf2image import convert_from_path

with open("secret.key", "rb") as key_file:  # Use 'rb' for binary read
    key = key_file.read()

f = Fernet(key)

def decode_img(img):
    try:
        decoded = decode(img)
        return f.decrypt(decoded[0].data).decode()
        
    except Exception as e:
        print(f"Error decoding image: {e}")


# Process PNG files as before
def no_pdf():
    for filename in os.listdir("qrcodes"):
        if filename.lower().endswith(".png"):
            img_path = os.path.join("qrcodes", filename)
            try:
                img = Image.open(img_path)
                print(decode_img(img))
            except Exception as e:
                print(f"Error loading {filename}: {e}")

#Process PDF file
pdf_path = os.path.join("qrcodes", "qrcodes.pdf")


def pdf():
    pdf_path = "qrcodes.pdf"
    if os.path.exists(pdf_path):
        try:
            # Convert PDF pages to images at 300 DPI for better detection
            pages = convert_from_path(pdf_path, dpi=300)
            for i, page in enumerate(pages):
                print(f"Decoding QR codes from PDF page {i+1}:")
                decoded_objs = decode(page)
                print(f"  Found {len(decoded_objs)} QR codes on this page.")
                for j, obj in enumerate(decoded_objs):
                    try:
                        decrypted = f.decrypt(obj.data).decode()
                        print(f"    QR {j+1}: {decrypted}")
                    except Exception as e:
                        print(f"    Error decoding QR {j+1}: {e}")
        except Exception as e:
            print(f"Error processing PDF: {e}")


# Main function to run the decryption process
#no_pdf()

pdf()