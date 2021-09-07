# Generate
import pyqrcode

url = pyqrcode.create("https://"+input("Website eingeben im format -> {Subdomain}.{Domain}.{top-level-domain}: "), error='H')
url.png("qrcode.png", module_color=(0, 0, 0, 255), background=(255, 255, 255, 255), scale=10)

input("Press any key to terminate the program")