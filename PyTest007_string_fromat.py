# 1.两个字符串连接
str1 = 'good'
str2 = 'bye'
print str1 + str2


# 2. 字符变量一个字符串相加
print 'very' + str1
print str1 + ' and ' + str2


# 3. 数字加文字  （不能直接连接）

num = 18
# print 'My age is' + num

        # 解决办法
        #一： 用str()把数字转换成字符串
print '一 My age is' + str(num)
        #二： 用%对字符串进行格式化  占位符
print '二 1 My age is %d' %6
print '二 2 My age is %d' %num

#  %d只能用来替换整数
#  %f  小数
#  %.2f  保留两位小数
#  %s  字符串
#
#

#
#
#

#
#
#
#
#
#

#
