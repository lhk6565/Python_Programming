# /연산자와 //연산자
from math import hypot


7 / 4
8 / 4

7 // 4
8 // 4
9 // 4

# 거듭제곱 연산자
bottom = float(input('직각삼각형의 밑변의 길이를 입력하시오: '))
height = float(input('직각삼각형의 높이를 입력하시오: '))
hypotenuse = (bottom**2 + height**2)**0.5
print('빗변은', hypotenuse, '입니다.')

# 복합 할당 연산자
num = 200
num += 100
num

num -= 100
num

num *= 20
num

num /= 2
num

# 비교 연산자
a, b = 100, 200
a == b
a != b
a > b
a < b
a >= b
a <= b