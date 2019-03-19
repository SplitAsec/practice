f1=open('abc.txt','w')
f1.write('''AAAAA
BBBBB
CCCCC
DDDDD
EEEEE''')
f1.close()
f1=open('abc.txt','r')
lines=f1.readlines()
lines.reverse()
f1.close()
f1=open('abc.txt','w')
for line in lines:
    line=line.strip()
    f1.write(line)
    f1.write('\n')
f1.close()
