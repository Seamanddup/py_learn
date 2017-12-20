# int(x) 把x转换成整数
# float(x) #把x转换成浮点数
# str(x) #把x转换成字符串
# bool(x) #把x转换成bool值

print 'Hello'+str(1)
print 'hello%d' % int('123')

#   在python中，其他类型转成 bool 类型时，以下数值会被认为是False：
#   为0的数字，包括0，0.0
#   空字符串，包括''，""
#   表示空值的None
#   空集合，包括()，[]，{}
#   其他的值都认为是True。



#   在if、while等条件判断语句里，判断条件会自动进行一次bool的转换。比如
#      a = '123'
#      if a:
#          print 'this is not a blank string'

#   这在编程中是很常见的一种写法。效果等同于
#   if bool(a)
#   或者
#   if a != ''
