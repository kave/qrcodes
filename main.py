import pyqrcode

# url = "https://mechanicode.io/careers-qr.html"
url = "https://mechanicode.io"

code = pyqrcode.create(url)

# code.png('code.png', scale=6)
# Inverts the color to background and white code
# code.png('code.png', scale=6, module_color='FFFFFF', background='000000')

code.png('code.png', scale=6)
