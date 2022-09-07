#grim, slop, xclip
from random import choice
import subprocess
import os
from string import ascii_uppercase

def coordinates():
    useless_cat_call = subprocess.run(["slop"], stdout=subprocess.PIPE, text=True)
    return useless_cat_call.stdout.replace("\n","")

coord = coordinates()


rStr = ''.join(choice(ascii_uppercase) for i in range(12))
rStr = rStr + '.png'


cord = coord.split('+')
os.system('grim -g "' + cord[1] + ', ' + cord[2] + ' ' + cord[0] + '" screenshot.png')

os.rename('screenshot.png', rStr)

import ftplib
host = str('ftp.host')
ftp_user = str('ftp.user')
ftp_password = str('ftp.password')

print('Попытка соединения с FTP-сервером', host)
#print('Login:', ftp_user)
#print('Password:', ftp_password)
ftp = ftplib.FTP('server', 'user', 'pass')


directory_list = ftp.nlst()
#print(directory_list)
file = str(rStr)
file_to_upload = open(file, 'rb')
ftp.storbinary('STOR ' + 'more.lumetas.ml/htdocs/screen/' + file, file_to_upload)
print('Файл', file, 'успешно загружен')

rStrR = 'http://more.lumetas.ml/screen/' + rStr
# шаблон ссылки
f = open('link', 'w')
f.write(rStrR)
f.close()



os.system("rm " + rStr)
print('Удалено')
os.system('xclip -sel clip link')
print('Скопировано')
