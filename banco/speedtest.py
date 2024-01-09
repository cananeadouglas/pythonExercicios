import math 
# sudo apt-get install python-pip
# pip install speedtest-cli
# pip install certifi

import speedtest

def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f'{size} Mbps'

wifi = speedtest()

print('obtendo velocidade de download... ')

download_speed = wifi.download()

print('obtendo velocidade de upload... ')

upload_speed = wifi.upload()

print('download', bytes_to_mb(download_speed))
print('upload', bytes_to_mb(upload_speed))