# coding:utf-8
# 二维码扫描

from qrtools import QR


def Scan_Qr(qr_img: str) -> bytes:
	qr = QR()
	qr.decode(qr_img)
	print(qr.data)
	return qr.data


print("Your Qr Code is: ", Scan_Qr("qr.png"))
