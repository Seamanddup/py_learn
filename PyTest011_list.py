print range(1,10)

l = range(1, 10)
#for i in l:
#    print i


#�б��е�Ԫ��Ҳ�����Ǳ�����ͣ����磺

x = ['meat', 'egg', 'fish', 'milk']

#�����ǲ�ͬ���͵Ļ�ϣ�

y = [365, 'everyday', 0.618, True]


mList = [365, 'everyday', 0.618, True]
print mList[0]


#����
for n in mList:
    print n
print"-------------------------"
#��
mList.append(1024)
print mList
print"-------------------------"
#ɾ
del mList[0]
print mList
print"-------------------------"
#��
mList[0] = 1111
print mList
print"-------------------------"
