r = []
s = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    r.append([name, score])
    r = sorted(r)
    s.append(score)
    s = sorted(list(set(s)))
for i in r:
    if i[1] == s[1]:
        print(i[0])
