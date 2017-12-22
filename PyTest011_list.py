print range(1,10)

l = range(1, 10)
#for i in l:
#    print i


#列表中的元素也可以是别的类型，比如：

x = ['meat', 'egg', 'fish', 'milk']

#甚至是不同类型的混合：

y = [365, 'everyday', 0.618, True]


mList = [365, 'everyday', 0.618, True]
print mList[0]


#遍历
for n in mList:
    print n
print"-------------------------"
#增
mList.append(1024)
print mList
print"-------------------------"
#删
del mList[0]
print mList
print"-------------------------"
#改
mList[0] = 1111
print mList
print"-------------------------"
