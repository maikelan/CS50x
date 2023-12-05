import csv #导入库

with open("favorites.csv","r") as file: #打开文件
    reader=csv.DictReader(file)#字典阅读器
    scratch,c,python=0,0,0
    counts={}
    for row in reader:
        favorite=row["language"]# 字典读取
        '''
        if favorite=="C":
            c+=1
        elif favorite=="Scratch":
            scratch+=1
        else:
            python+=1
        '''
    if favorite in counts:
        counts[favorite]+=1
    else counts[favorite]=1
    '''
    print(f"scrathch:{scratch}")# 格式化打印
    print(f"c:{c}")
    print(f"python:{python}")
    '''
    for i in counts:
        print(f"{i}:{counts[i]}")





