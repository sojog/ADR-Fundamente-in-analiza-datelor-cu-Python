import pyqrcode

url = "..."
qrcode = pyqrcode.create(url)
img = qrcode.png("ana.png", scale=5)
