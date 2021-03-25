import pyqrcode
url = pyqrcode.create('Endereço web aqui.')# ESSA LINHA DE COMANDO VAI ADICIONAR O LINK NO QR_CODE.
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
url.png("BIGTIGERQRCode.png",scale=6) # VAI CRIAR UMA IMAGEM EM PNG DO QR_CODE.
print(url.terminal(quiet_zone=1))
