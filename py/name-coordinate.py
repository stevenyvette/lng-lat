# coding=utf-8
#整理输出所有出现过的企业
#格式：
# name：{lng：，lat：}
all_location={}
month=["Junnode-res.txt","Aprnode-res.txt","Augnode-res.txt","Maynode-res.txt","Marnode-res.txt","Julnode-res.txt"]

out=open('../data/name-coordinate-res.txt', 'w')

for x in month:
    i="../data/res/old/"+x
    print i
    f=open(i,'r')
    for line in f.readlines():
        try:
            tmp=line.split(',')
            if not all_location.has_key(tmp[0]):
                all_location[tmp[0]]={"lng":tmp[1],"lat":tmp[2][:-1]}
        except:
            print line
    f.close()

for key in all_location:
    out.write(key+':{"lng":'+all_location[key]["lng"]+',"lat":'+all_location[key]["lat"]+'}\n')

out.close()


