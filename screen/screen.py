from random import choice
from string import ascii_uppercase

rStr = ''.join(choice(ascii_uppercase) for i in range(12))
rStr = rStr + '.png'
import glob
import os
import pyautogui
screen = pyautogui.screenshot('screenshot.png')
print(screen)
os.rename('screenshot.png', rStr)

import ftplib
host = str('ftp.host')
ftp_user = str('ftp.user')
ftp_password = str('ftp.password')

print('Попытка соединения с FTP-сервером', host)
#print('Login:', ftp_user)
#print('Password:', ftp_password)
ftp = ftplib.FTP(host, ftp_user, ftp_password)


directory_list = ftp.nlst()
#print(directory_list)
file = str(rStr)
file_to_upload = open(file, 'rb')
ftp.storbinary('STOR ' + 'путь/относительно/папки/ftp/сервера/screen/' + file, file_to_upload)
print('Файл', file, 'успешно загружен')

rStrR = 'http://domen.com/screen/' + rStr
# шаблон ссылки
f = open('link', 'w')
f.write(rStrR)
f.close()



os.system("rm " + rStr)
print('Удалено')
os.system('xclip -sel clip link')
print('Скопировано')
