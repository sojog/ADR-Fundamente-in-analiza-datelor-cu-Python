import pyqrcode

url = "www.youtube.com/@SilviuOjog"
qrcode = pyqrcode.create(url)
img = qrcode.png("test.png", scale=5)
