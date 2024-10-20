import qrcode
url = "https://github.com/Praisel04/VirtualMachine/tree/main"

qr = qrcode.QRCode(version=1, box_size= 10, border=2)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image()
img.save("qrcode.png")