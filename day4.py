f = open('day4.txt')
lines = [l.strip().split(',') for l in f.readlines()]

res1 = 0
res2 = 0

for l in lines:
    a1, a2 = [int(el) for el in l[0].split('-')]
    b1, b2 = [int(el) for el in l[1].split('-')]

    if a1 <= b1 and a2 >= b2 or b1 <= a1 and b2 >= a2:
        res1 += 1

    print(len(set(range(a1, a2+1)) & set(range(b1, b2+1))))

print('part1: ', res1)
print('part2: ', res2) 