# coding=utf-8

a=["Mar","Apr","May","Jun","Jul","Aug"]

out=open("../data/res/month-district-res.txt",'w')
for i in a:
    file="../data/res/"+i+"-result-final.txt"
    f=open(file,'r')
    retailer=[]
    catering=[]
    manufacturer=[]
    wholesaler=[]
    farmer=[]
    unknown=[]

    out.write(i + "\n")
    count=1
    for line in f.readlines():
        if count==15 or count==16:
            count+=1
            continue
        try:
            tmp=line.split(',')
            t1=tmp[1].find(':')
            retailer.append(tmp[1][t1+1:])
            t2=tmp[2].find(':')
            catering.append(tmp[2][t2+1:])
            t5 = tmp[5].find(':')
            manufacturer.append(tmp[5][t5 + 1:])
            t4 = tmp[4].find(':')
            wholesaler.append(tmp[4][t4 + 1:])
            t3 = tmp[3].find(':')
            farmer.append(tmp[3][t3 + 1:])
            t0 = tmp[0].find(':')
            unknown.append(tmp[0][t0 + 1:])
            count+=1
        except:
            count+=1
            continue
    out.write("retailer")
    for content in retailer:
        out.write(content+',')
    out.write('\n')
    out.write("catering")
    for content in catering:
        out.write(content + ',')
    out.write('\n')
    out.write("manufacturer")
    for content in manufacturer:
        out.write(content + ',')
    out.write('\n')
    out.write("wholesaler")
    for content in wholesaler:
        out.write(content + ',')
    out.write('\n')
    out.write("farmer")
    for content in farmer:
        out.write(content + ',')
    out.write('\n')
    out.write("unknown")
    for content in unknown:
        out.write(content + ',')

    out.write('\n')




