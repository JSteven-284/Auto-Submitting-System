import csv
import os

def saveInfoList(infoList):
    if os.path.exists("data.csv"):
        os.remove("data.csv")
    ip1, ip2, time, method = infoList[0], infoList[1], infoList[2], infoList[3]

    # read name1 name2 from csv
    headers = ['1','2','3','4','5','6']
    rows = [(time, ip1, ip2, method, "name1", "name2"),
            ('（图片一）','（图片二）','（图片三）')]
    with open('data.csv','w',encoding='utf8',newline='') as f :
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)