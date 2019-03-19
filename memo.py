input1 = input('Please enter your message:  ')
f1=open('test.txt','r')
if f1:
    f1.close()
    f1 = open('test.txt','a')
else:
    f1.close()
    f1 = open('test.txt', 'w')
f1.write(input1)
f1.write('\n')
f1.close()
