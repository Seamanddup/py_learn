sentence = 'I am an Englist sentence'
x=sentence.split()
print x
# ��� ['I', 'am', 'an', 'Englist', 'sentence']

# split() �ᰴ�� �ո� \n \t ���зָ�

print "------------------------------------------"

section = 'Hi. I am the one. Bye.'
y=section.split(".")
print y
# ��� ['Hi', ' I am the one', ' Bye', ''] ע���������հ׵��ַ���


print "------------------------------------------"

z='aaa'.split('a')
print z
# ��� ['', '', '', '']
