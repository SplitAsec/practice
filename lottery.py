import random,time
def random_pop(data):
    number = random.randint(0,len(data)-1)
    return data.pop(number)
lotto = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
tried = 0
print('두구두구두구... 오늘의 로또 예상번호는..!!!!')
time.sleep(3)
while tried <  6:
    tried   += 1
    print(f'{tried}번',random_pop(lotto))
    if tried == 6:
        print('이상 예상번호였습니다!')
    time.sleep(3)
