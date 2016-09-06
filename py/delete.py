# coding=utf-8

f=open("../data/data_months/all_Junnode.csv","r")
out=open("../data/res/Junnode-res.txt","w")

res={}
for line in f.readlines():
    try:
        tmp=line.split(",")
        res[tmp[0]]=[tmp[1],tmp[2]]
    except:
        continue

for key in res:
    out.write(key+","+str(res[key][0])+","+str(res[key][1]))