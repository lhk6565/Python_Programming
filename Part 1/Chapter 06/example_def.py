def print_address():
    print('경상북도')
    print('울릉군 울릉읍')
    print('독도리 산 1-96번지')

print(print_address())

# 여러개 값 리턴 받기
def calc(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2

n1, n2 = 200, 100
t1, t2, t3, t4 = calc(n1, n2)
print(n1, '+', n2, '=', t1)
print(n1, '-', n2, '=', t2)
print(n1, '*', n2, '=', t3)
print(n1, '/', n2, '=', t4)

#함수에 쉽게 일을 시키는 디폴트 인자
def order(num, pickle = True, onion = True):
    print('햄버거 {0} 개 - 피클 {1}, 양파 {2}'.format(num, pickle, onion))

order(1, False, True)

#키워드 인자로 더욱더 고급지게 함수 활용하기
def power(base, exponent):
    return base**exponent

power(2, 10)