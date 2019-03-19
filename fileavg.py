with open('sample.txt', 'r') as sample:
    samr = sample.readlines()
    total = 0
    for num in samr:
        n = int(num.strip())
        total += n
avg = total / len(samr)
with open('result.txt', 'w') as result:
    result.write(str(avg))
