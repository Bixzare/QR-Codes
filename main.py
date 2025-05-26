import qrcode
from placeholder import ids,names
from cryptography.fernet import Fernet

with open("secret.key") as key_file:
    key = key_file.read()
# key = Fernet.generate_key()

# # Optionally save the key
# with open("secret.key", "wb") as key_file:
#     key_file.write(key)

# # Step 2: Load the key (use this whenever encrypting/decrypting)
# with open("secret.key", "rb") as key_file:
#     key = key_file.read()

f = Fernet(key)

id = list(ids)
n = list(names)

res = []
for i in range(len(id)):
    res.append(id[i] + " " + n[i][0] +" "+ n[i][1])
    

def qr_gen(res,n):
    for i in range(len(res)):
        message = res[i].encode()
        token = f.encrypt(message)
        img = qrcode.make(token)
        img.save("qrcodes/"+n[i][0]+".png")




qr_gen(res,n)
# lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


# message = lorem.encode()

# token = f.encrypt(message)

# img = qrcode.make(token)

# img.save("qr_code.png")


# print("Encrypted message:", token)

# decrypted = f.decrypt(token).decode()

# print("Decrypted message:", decrypted)

