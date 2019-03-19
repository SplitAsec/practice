f1 = open('test.txt', 'r')
text = f1.readlines()
f1.close()
text[1] = text[1].replace('java', 'python')
f1 = open('test.txt', 'w')
for line in text:
    f1.write(line)
f1.close()
