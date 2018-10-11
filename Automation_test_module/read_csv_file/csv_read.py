import csv
import os
csvfile=os.path.dirname(os.getcwd())+'\\read_csv_file\\'
date=csv.reader(open(csvfile+'info.csv','r'))
for user in date:
    if(user[0]==''):
        print('空数据')
    else:
        print(user[0])