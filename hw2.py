#比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異
'''
File I/O print 每一列出來的type是str，CSV Reader print 每一列出來的type是list
'''
#import需要的libarary
import urllib.request
import os, sys
import csv
import json

#下載指定檔案
res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
urllib.request.urlretrieve(res, './Data/example.csv')

#開啟csv檔
rawdata = []
with open('./Data/example.csv', newline='',encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        rawdata.append(row)
    #print(rawdata)

#取出各班次的每一個時間，分別存取
for i in range(1,len(rawdata)):
    if i == 1: #避免多一個逗號
        dict1 = {rawdata[0][5] : rawdata[i][5]}
        dict2 = {rawdata[0][6] : rawdata[i][6]}
        dict3 = {rawdata[0][7] : rawdata[i][7]}
        dict4 = {rawdata[0][8] : rawdata[i][8]}
        dict5 = {rawdata[0][9] : rawdata[i][9]}
    else:
        dict1[rawdata[0][5]] = str(dict1.get(rawdata[0][5])) + ' , '+ rawdata[i][5]
        dict2[rawdata[0][6]] = str(dict2.get(rawdata[0][6])) + ' , '+ rawdata[i][6]
        dict3[rawdata[0][7]] = str(dict3.get(rawdata[0][7])) + ' , '+ rawdata[i][7]
        dict4[rawdata[0][8]] = str(dict4.get(rawdata[0][8])) + ' , '+ rawdata[i][8]
        dict5[rawdata[0][9]] = str(dict5.get(rawdata[0][9])) + ' , '+ rawdata[i][9]

#將班次一到五與其所有時間用個別一種資料型態保存
json_string1 = json.dumps(dict1, ensure_ascii=False)#避免變成亂碼
json_string2 = json.dumps(dict2, ensure_ascii=False)
json_string3 = json.dumps(dict3, ensure_ascii=False)
json_string4 = json.dumps(dict4, ensure_ascii=False)
json_string5 = json.dumps(dict5, ensure_ascii=False)

print(json_string1,json_string2,json_string3,json_string4,json_string5)

