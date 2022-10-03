st = 'I love Python Programming'
for ch in st:
    if ch in ['a','e','i','o','u', 'A','E','I','O','U']:
        continue
    print(ch, end = '')