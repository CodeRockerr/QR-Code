import qrcode as qr
img = qr.make("https://coderockerr.github.io/my-portfolio/")
img.save("my_webpage.png")