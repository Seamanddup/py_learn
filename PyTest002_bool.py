#   >������
#   <��С��
#   >=�����ڵ���
#   <=��С�ڵ���
#   ==�����ڡ��Ƚ�����ֵ�Ƿ���ȡ�֮�����������Ⱥţ���Ϊ�˺ͱ�����ֵ���ֿ�����
#   !=��������

#   ����һ���߼��������

#   not���߼����ǡ������xΪTrue����not xΪFalse
#   and���߼����롱�����xΪTrue����yΪTrue����x and yΪTrue
#   or���߼����򡱡����x��y��������һ��ΪTrue����x or yΪTrue

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
