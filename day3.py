f = open('day3.txt')
lines = [l.strip() for l in f.readlines()]
res = 0

for l in lines:
    h = int(len(l)/2)
    a = set(l[:h])
    b = set(l[h:])
    for c in a:
        if c in b:
            if c.islower():
                res += ord(c) - 96
            else:
                res += ord(c) - 38

print(res)

