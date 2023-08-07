import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=10,)
qr.add_data("https://coderockerr.github.io/my-portfolio/")
qr.make(fit=True)
img = qr.make_image(fill_color="blue")
img.save("my_webpage2.png")