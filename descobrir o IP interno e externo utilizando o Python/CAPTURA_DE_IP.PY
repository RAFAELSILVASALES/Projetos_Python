import socket
from requests import get
pc= socket.gethostname()
ipInterno= socket.gethostbyname(pc)
ipExterno= get('https://api.ipify.org').text
print("/n Nome do PC:", pc)
print("/n IP |Interno:",ipInterno)
print("/n IP |Extreno:",ipExterno)
