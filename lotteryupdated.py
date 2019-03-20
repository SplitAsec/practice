import random
import time


def random_pop(data):  #random picker
    number = random.randint(1, len(data)-1)
    return data.pop(number)


lotto = list(range(1, 46))
seq = 1
picks = []
input1 = input('어느 방식으로 복권을 구매하시겠습니까? (자동 / 수동) : ') #aksing automatic or manual
while input1:
    if input1 == '자동': #in case automatic
        while seq <= 6:
            num = random_pop(lotto)
            print(f'{seq} : {num}')
            picks.append(num)
            seq += 1
    elif input1 == '수동': #in case manual
        while seq <= 6: #looping number picking 6 times
            pick = input(f'{seq}번 숫자를 골라주세요 : ') 
            pickn = int(pick)
            while pick:
                if pickn in picks: #already chosen number, requesting another number
                    print('고르지 않은 숫자를 골라주세요.') 
                    break
                elif pickn not in lotto: #out of range. requesting another number
                    print('1~45 사이의 숫자를 골라주세요.') 
                    break
                else: #chosen legal number, continue loop
                    print(f'{seq}번에 {pickn}을/를 고르셨습니다.')
                    picks.append(pickn)
                    seq += 1
    else: #wrong input; asking once again.
        input1 = input("'자동' 또는 '수동'을 입력해주세요 : ")
        continue
    break
print('추첨을 시작합니다.')
time.sleep(3)
lotto = list(range(1, 46)) #resetting list for drawing
seq = 1
chosenlist = [] #list for drawn number/comparison
while seq <= 7:
    chosen = random_pop(lotto) #pulling random number out of list
    if seq < 7:
        print(f'{seq}번 {chosen}')
    else:
        print(f'보너스 번호는 {chosen}입니다.')
    chosenlist.append(chosen) #adding drawn number into list
    seq += 1
    time.sleep(3)
hit = 0
for match in range(1, 6): #comparison loop
    if picks[match] == chosenlist[match]: 
        hit += 1 #number of won numbers
bonus = False
try:
    if picks.index(chosenlist[-1]):
        bonus = True
except:
    bonus = False
if hit == 6:
    print('축하합니다! 1등에 당첨되셨습니다!') #1st place. hit 6 times
elif hit == 5:
    if bonus:
        print('축하합니다! 2등에 당첨되셨습니다!') #2nd place. hit 5 times + bonus
    else:
        print('축하합니다! 3등에 당첨되셨습니다!') #3rd place. hit only 5 times
elif hit == 4:
    print('축하합니다! 4등에 당첨되셨습니다!') #4th place. hit only 4 times
elif hit == 3:
    print('축하합니다! 5등에 당첨되셨습니다!') #5th place. hit only 5 times.
else:
    print('아쉽습니다. 꽝입니다.') #No prize for you :P
