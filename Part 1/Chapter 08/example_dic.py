# 키와 값을 가진 딕셔너리로 자료를 저장하자
from re import S


phone_book = {'홍길동': '010-1234-5678'}
phone_book['강감찬'] = '010-1234-5679'
phone_book['이순신'] = '010-1234-5680'
print(phone_book)

# 딕셔너리의 기능을 알아보자
phone_book.keys()
phone_book.values()
phone_book.items()
for name, phone_num in phone_book.items():
    print(name, ':', phone_num)

f = open('hello.txt', 'w')
f.write('Hello World!')
f.close()
f = open('hello.txt', 'r')
s = f.read()
print(s)
f.close()