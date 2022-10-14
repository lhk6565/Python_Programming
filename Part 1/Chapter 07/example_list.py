letters = ['A', 'B', 'C', 'D', 'E', 'F']
letters[2:5]
letters[:3]
letters[3:]
letters[:]

# 리스트의 객체의 생성과 참조라는 깊이있는 개념
alist = ['Kim', 'Park', 'LEE', 'Hong']
blist = alist[:]
id(alist)
id(blist)

# 리스트를 탐색해보자
bts = ['V', 'J-Hope', 'Suga', 'Jungkook']
bts.index('Suga')

if 'suga' in bts:
    print(bts.index('Suga'))

for member in bts:
    print(member)

# 리스트를 크기에 따라 정렬해보자
numbers = [9, 6 ,7, 1, 8, 4, 5, 3, 2]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# 리스트 함축은 코드를 짧고 간결하게 만드는데 사용된다
[x**2 for x in [1, 2, 3, 4, 5]]

[x for x in range(10)]
[x*x for x in range(10)]
st = 'Hello World'
[x.upper() for x in st]

a = ['welcome', 'to', 'the' ,'python', 'world']
first_a = [s[0].upper() for s in a]
print(first_a)

# 조건이 붙는 리스트 함축 표현도 가능하다.
[int(x) for x in input('정수를 여러개 입력하세요 : ').split()]
[int(x) for x in input('정수를 여러개 입력하세요 : ').split() if x.isdigit()]

[(x,y) for x in [1, 2, 3] for y in [3, 1, 4]]
[(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]