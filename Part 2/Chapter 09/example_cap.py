# 대문자와 소문자 변환, 그리고 문자열 삭제
s = 'Hello, World!'
s.lower()
s.upper()

s = '         Hello, World!         '
s.strip()
s.lstrip()
s.rstrip()

s = '###########this is an example###########'
s.strip('#').capitalize()

s = 'www.booksr.co.kr'
s.find('.kr')
s.find('x')