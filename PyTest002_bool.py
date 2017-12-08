#   >：大于
#   <：小于
#   >=：大于等于
#   <=：小于等于
#   ==：等于。比较两个值是否相等。之所以用两个等号，是为了和变量赋值区分开来。
#   !=：不等与

#   还有一种逻辑运算符：

#   not：逻辑“非”。如果x为True，则not x为False
#   and：逻辑“与”。如果x为True，且y为True，则x and y为True
#   or：逻辑“或”。如果x、y中至少有一个为True，则x or y为True

num = 10
print 'Guess what I think?'
answer = int(input())

result = answer<num
print 'too small?'
print result

result = answer>num
print 'too big?'
print result

result = answer==num
print 'equal?'
print result
