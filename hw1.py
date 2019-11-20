#簡答題
'''檔案、API、爬蟲的不同:
1. 檔案資料會包成檔案提供下載，格式可能包含常⽤用的標準格式，例例如「CSV」、「JSON」等等通⽤用的格式。
2. 開放接口（API）提供程式化的連接的接口，讓工程師/分析師可以選擇資料中要讀取的特定部分，⽽而不需要把整批資料事先完整下載回來
3. 網頁爬蟲資料沒有以檔案或 API 提供，但出現在網⾴頁上。可以利用爬蟲程式，將網頁的資料解析所需的部分。
前兩者是資料擁有者主動提供，後者則是被動'''

#實作
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
