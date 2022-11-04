# 문자열을 이어붙이는 것은 파이썬한테는 쉬운 일
','.join(['apple', 'grape', 'banana'])
'-'.join('010.1234.5678'.split('.'))
'010.1234.5678'.replace('.','-')

s = 'hello world'
clist = list(s)
clist
''.join(clist)

a_string = 'Actions \n\t speak louder than words'
a_string
print(a_string)
world_list = a_string.split()
world_list
refined_string = ' '.join(world_list)
refined_string