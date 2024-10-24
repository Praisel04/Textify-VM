#Import the QRCODE library.

import qrcode

#Define the URL of the place that you want to access
url = "https://github.com/Praisel04/VirtualMachine/tree/main"

#Define de QRCode, size, version and border
qr = qrcode.QRCode(version=1, box_size= 10, border=2)

#Link the URL with the QRCode and make the info fit.
qr.add_data(url)
qr.make(fit=True)

#Generate the image and save it with a name.
img = qr.make_image()
img.save("qrcode.png")