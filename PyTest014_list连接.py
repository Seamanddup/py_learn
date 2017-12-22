# join的格式有些奇怪，它不是list的方法，而是字符串的方法
s = ';'
li = ['apple', 'pear', 'orange']
fruit = s.join(li)
print fruit

#   得到结果'apple;pear;orange'
print "----------------------------"


''.join(['hello', 'world'])

#   得到'helloworld'，字符串被无缝连接在一起。
