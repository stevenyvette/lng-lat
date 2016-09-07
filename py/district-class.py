# coding=utf-8
f=open('location-res.txt','r')
out=open('district-sh.txt','w')

count={' 黄浦区':0,' 卢湾区':0,' 徐汇区':0,' 长宁区':0,' 静安区':0,
' 普陀区':0,' 闸北区':0,' 虹口区':0,' 杨浦区':0,' 宝山区':0,
' 闵行区':0,' 嘉定区':0,' 浦东新区':0,' 松江区':0,' 金山区':0, ' 青浦区':0,' 南汇区':0,' 奉贤区':0,' 崇明县':0,'out':0}
total=0
for line in f.readlines():
	tmp=line.split(',')
	#print tmp[3]
	if(count.has_key(tmp[3])):
		count[tmp[3]]+=1
		
	else:
		count['out']+=1

for key in count:
	out.write(key+':')
	out.write(str(count[key])+'\n')
	total+=count[key]
print total
f.close()
out.close()
