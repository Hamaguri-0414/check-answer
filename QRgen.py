import sys
import qrcode
import hashlib

args = sys.argv
if len(args) != 2:
    print("Usage: python QRgen.py [answer]")

ans_sha256 = hashlib.sha256(args[1].encode()).hexdigest()
URL = "https://hamaguri-0414.github.io/check-answer?answer=" + ans_sha256
print(URL)

qr = qrcode.make(URL)
qr.save("QRcode.png")
