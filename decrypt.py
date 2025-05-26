from cryptography.fernet import Fernet
from PIL import Image
from pyzbar.pyzbar import decode
import os

with open("secret.key") as key_file:
    key = key_file.read()

f = Fernet(key)

def decode_img(img):
    try:
        decoded = decode(img)
        return f.decrypt(decoded[0].data).decode()
        
    except Exception as e:
        print(f"Error decoding image: {e}")


for filename in os.listdir("qrcodes"):
    if filename.lower().endswith(".png"):
        img_path = os.path.join("qrcodes", filename)
        try:
            img = Image.open(img_path)
            print(decode_img(img))
        except Exception as e:
            print(f"Error loading {filename}: {e}")

