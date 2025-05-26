import qrcode
from placeholder import ids,names
from cryptography.fernet import Fernet
import os
key_path = "secret.key"

# Check if the key already exists
if not os.path.exists(key_path):
    # Generate a new key and save it
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
else:
    # Load the existing key
    with open(key_path, "rb") as key_file:
        key = key_file.read()


f = Fernet(key)

id = list(ids)
n = list(names)

res = []
for i in range(len(id)):
    res.append(id[i] + " " + n[i][0] +" "+ n[i][1])
    

def qr_gen(res,n,pdf:bool=False):
    images = []
    for i in range(len(res)):
        message = res[i].encode()
        token = f.encrypt(message)
        img = qrcode.make(token)
        if(pdf):
            images.append(img.convert("RGB"))  # Convert to RGB for PDF compatibility
        else:
            # Ensure the 'qrcodes' directory exists
            if not os.path.exists("qrcodes"):
                os.makedirs("qrcodes")
            img.save("qrcodes/"+n[i][0]+".png")
    
    if pdf:
        images[0].save(
            "qrcodes.pdf",
            save_all=True,
            append_images=images[1:]
        )
        print("PDF saved as qrcodes.pdf")
    else:
        print("Images in qrcodes folder.")




# remove pdf to get just images
qr_gen(res,n)

