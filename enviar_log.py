import socket
from datetime import datetime
import requests
import os

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
ano = datetime.now().strftime("%Y")
mes = datetime.now().strftime("%m")

with open(r"C:\Program Files (x86)\PaperCut Print Logger\logs\sheet-count-" 
          + ano + "-" + mes + ".txt") as f:
  log = f.read()

url = "http://192.168.200.66:5000/atualizar"  # IP do servidor

dados = {
    "hostname":  hostname,
    "ip": ip,
    "log": log
}

res = requests.post(url, json=dados)
print("Resposta do servidor:", res.text)
