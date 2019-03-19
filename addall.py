input1 = input('숫자를 입력하세요: ')
numbers = input1.split(',')
total = 0
for n in numbers:
    num = int(n)
    total+=num
print(total)

