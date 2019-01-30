import paramiko, pprint
from pip._vendor.distlib.compat import raw_input

host = '192.168.0.0'
user = 'usuario'
passwd = 'senha da maquina'

# conecção

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    comando = raw_input('comando: ')
    entrada, saida, erros = client.exec_command(comando)
    pprint.pprint(saida.readlines())