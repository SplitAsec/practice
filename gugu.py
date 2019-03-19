input1 = input('구구단을 출력할 숫자를 입력하세요(2~9): ')
mlt = range(1,10)
num = int(input1)
for m in mlt:
    n = num * m
    print(n, end=' ')
