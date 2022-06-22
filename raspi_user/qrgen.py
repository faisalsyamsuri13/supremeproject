import qrcode
import keygen
import socket

ip_address = socket.gethostbyname(socket.gethostname())
pub_key = keygen.key
url = "http://{}/supremeproject/key.php?key={}".format(ip_address, pub_key)
target = './qf/qrcode_{}.png'.format(url.split('?')[1])
qr = qrcode.QRCode(version=1, box_size=10, border=1)
qr.add_data(url)
qr.make(fit=True)
def generate():
    try:
        img = qr.make_image(fill='black', back_color='white')
        img.save(target)
        print("- QRCode successfully generated!")
    except Exception as e:
        print("Failed to generate QRCode. Please check the qrqen.py module. Error: {}".format(e))
