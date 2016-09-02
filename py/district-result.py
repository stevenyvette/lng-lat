# coding=utf-8

f=open("../data/res/Jul-dis-res.txt","r")
f1=open("../data/type.txt","r")
out=open("../data/res/Jul-result-final.txt","w")

type={}
dic={"黄浦区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},
     "卢湾区": {"": 0, "retailer": 0, "catering": 0, "manufacturer": 0, "farmer": 0, "wholesaler": 0},"徐汇区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"长宁区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"静安区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"普陀区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"闸北区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"虹口区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"杨浦区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"宝山区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"闵行区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"浦东新区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"嘉定区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"松江区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"金山区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},"崇明县区":{"":0,"retailer":0,"catering":0,"manufacturer":0,"farmer":0,"wholesaler":0},}
for line in f1.readlines():
    try:
        tmp=line.split(",")
        type[tmp[0]]=tmp[1][:-1]
    except:
        continue

print len(type)

for line in f.readlines():
    try:
        tmp=line.split(",")
        dic[tmp[5][1:-1]][type[tmp[0]]]+=1
    except:
        continue

print dic["徐汇区"]["catering"]
for key in dic:
    out.write(key+":\n")
    for key2 in dic[key]:
        out.write(key2+":"+str(dic[key][key2])+",")
    out.write("\n")

f.close()
out.close()
f1.close()



