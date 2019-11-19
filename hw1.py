#根據需求引入正確的Libary
from urllib.request import urlretrieve
import os,sys

#下載檔案到data資料夾，存檔為homework.txt
try:
    os.makedirs('./Data/',exist_ok=True)
    urlretrieve("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./Data/Homework.txt")    
except:
    print('error')

#確認Data資料夾中有Homework.txt的檔案
files = []
dirs = os.listdir('./')
for file in dirs:
    files.append(file)

if 'Homework.txt' in files:
    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')

#將'hello world'字串填寫到檔案中
f =''
with open("./Data/Homework.txt", "w") as fh:
    f = fh.write('Hello World')

try:
    with open("./Data/Homework.txt","r") as fh:
        f = fh.read()
        print(f)

except EnvironmentError:
    pass

#檢查檔案字數是否符合hello world

if len('Hello World') == len(f):
    print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
else:
    print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
