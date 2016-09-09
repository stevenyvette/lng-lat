# coding=utf-8
#输出每个月各个品类的企业在区域分布上的数量

a=["3","4","5","6","7","8"]

retailertmp = []
cateringtmp = []
manufacturertmp = []
wholesalertmp = []
farmertmp = []
unknowntmp = []

out=open("../data/res/month-district-res.txt",'w')
for i in a:
    file="../data/res/month-category-"+i+"-test.txt"
    f=open(file,'r')
    retailer = []
    catering = []
    manufacturer = []
    wholesaler = []
    farmer = []
    unknown = []
    count=1
    for line in f.readlines():
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

    retailertmp.append(retailer)
    cateringtmp.append(catering)
    manufacturertmp.append(manufacturer)
    wholesalertmp.append(wholesaler)
    farmertmp.append(farmer)
    unknowntmp.append(unknown)

out.write("retailer\n")
count=3
for content in retailertmp:
    out.write(str(count)+":[")
    for i in content:
        out.write(i+',')
    out.write('],\n')
    count+=1
out.write("catering\n")
count=3
for content in cateringtmp:
    out.write(str(count) + ":[")
    for i in content:
        out.write(i + ',')
    out.write('],\n')
    count += 1
out.write("manufacturer\n")
count=3
for content in manufacturertmp:
    out.write(str(count) + ":[")
    for i in content:
        out.write(i + ',')
    out.write('],\n')
    count += 1
out.write("wholesaler\n")
count=3
for content in wholesalertmp:
    out.write(str(count) + ":[")
    for i in content:
        out.write(i + ',')
    out.write('],\n')
    count += 1
out.write("farmer\n")
count=3
for content in farmertmp:
    out.write(str(count) + ":[")
    for i in content:
        out.write(i + ',')
    out.write('],\n')
    count += 1
out.write("unknown\n")
count=3
for content in unknowntmp:
    out.write(str(count) + ":[")
    for i in content:
        out.write(i + ',')
    out.write('],\n')
    count += 1




