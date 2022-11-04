# split() 메소드는 문자열을 잘 잘라줘요
s = 'Welcome to Python'
s.split()
s = 'Hello, World'
s.split('.')

s = 'Hello, World!'
s.split(', ')
s = 'Welcome, to, Python, and , bla, bla  '
[x.strip() for x in s.split(',')]