from collections import defaultdict

f = open('day1.txt')
lines = f.readlines()

la, lb = [], []

for l in lines:
    l = l.split()
    print(l)
    la.append(int(l[0]))
    lb.append(int(l[1]))

count = defaultdict(int)
for i in range(len(lb)):
    count[lb[i]] += 1

la.sort()
lb.sort()
diff = 0
similarity = 0
for i in range(len(la)):
    diff += abs(la[i] - lb[i])
    similarity += count[la[i]] * la[i]

print(diff, similarity)
