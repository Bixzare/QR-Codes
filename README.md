install requirements 

run main.py to generate qr codes using placeholder (for now)

run decrypt.py to decrypt qrcodes 

TBD:
fast api server 
database


pdf:

Download Poppler for Windows:

Go to: https://github.com/oschwartz10612/poppler-windows/releases/
Download the latest poppler-xx_xx_xx-xxx.zip release.
Extract the ZIP file to a folder, e.g., C:\poppler.

Add the bin folder to your system PATH:

Open Windows Search, type "Environment Variables", and open "Edit the system environment variables".
Click "Environment Variables".
Under "System variables", find and select "Path", then click "Edit".
Click "New" and add the path to the bin folder, e.g., C:\poppler\bin.
Click OK to close all dialogs.
Restart your terminal or VS Code.

After this, your script should work and be able to process the PDF. Let me know if you want step-by-step screenshots or further help!