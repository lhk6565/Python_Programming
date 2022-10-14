# 순서가 중요하지 않은 대상들이 모이면 : 집합
numbers = {2, 1, 3}
print(numbers)

set([1, 2, 3, 1, 2,])
set('abcdefa')

# 집합에 적용할 수 있는 다양한 연산들을 살펴보자
a_set = {1, 5, 4, 3, 7, 4}
len(a_set)
max(a_set)
min(a_set)
sorted(a_set)
sum(a_set)

# 풍부하고 멋진 집합 연산이 있다
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
A.union(B)

print(A & B)
A.intersection(B)

print(A - B)
A.difference(B)

print(A ^ B)
A.symmetric_difference(B)