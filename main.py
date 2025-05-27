import qrcode
from placeholder import ids,names
from cryptography.fernet import Fernet
import os
from PIL import Image

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

qr = qrcode.QRCode(
     version=None,
     error_correction=qrcode.constants.ERROR_CORRECT_L,
     box_size=8, # 9 is 4, 8 is 6
     border=4
 )   

def qr_gen(res, n, pdf: bool = False):
    images = []
    for i in range(len(res)):
        message = res[i].encode()
        token = f.encrypt(message)
        qr.add_data(token)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        if pdf:
            images.append(img)
        else:
            if not os.path.exists("qrcodes"):
                os.makedirs("qrcodes")
            img.save("qrcodes/" + n[i][0] + ".png")
        qr.clear()
    if pdf:
        # A4 size at 300 DPI
        PAGE_WIDTH, PAGE_HEIGHT = 2480, 3508
        if images:
            qr_w, qr_h = images[0].size
            # Calculate how many QR codes fit per row and column
            cols = PAGE_WIDTH // qr_w
            rows = PAGE_HEIGHT // qr_h
            max_per_page = cols * rows
            canvases = []
            for page_start in range(0, len(images), max_per_page):
                canvas = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), "white")
                for idx, img in enumerate(images[page_start:page_start+max_per_page]):
                    x = (idx % cols) * qr_w
                    y = (idx // cols) * qr_h
                    canvas.paste(img, (x, y))
                canvases.append(canvas)
            canvases[0].save(
                "qrcodes.pdf",
                save_all=True,
                append_images=canvases[1:],
                resolution=300.0
            )
            print(f"PDF saved as qrcodes.pdf with {len(images)} QR codes across {len(canvases)} page(s).")
        else:
            print("No images to save.")
    else:
        print("Images in qrcodes folder.")




# remove pdf to get just images
# qr_gen(res,n)
qr_gen(res,n,pdf=True)

