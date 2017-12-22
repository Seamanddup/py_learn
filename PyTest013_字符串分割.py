sentence = 'I am an Englist sentence'
x=sentence.split()
print x
# 输出 ['I', 'am', 'an', 'Englist', 'sentence']

# split() 会按照 空格 \n \t 进行分割

print "------------------------------------------"

section = 'Hi. I am the one. Bye.'
y=section.split(".")
print y
# 输出 ['Hi', ' I am the one', ' Bye', ''] 注意最后这个空白的字符串


print "------------------------------------------"

z='aaa'.split('a')
print z
# 输出 ['', '', '', '']
