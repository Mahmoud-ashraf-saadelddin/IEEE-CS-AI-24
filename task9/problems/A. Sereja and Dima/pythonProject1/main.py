n = int(input())
arr = list(map(int, input().split()))
d = []
s = []
flag = 0
if len(arr) % 2 != 0:
    if arr[-1] > arr[0]:
        first = arr[-1]
        arr.remove(first)
        s.append(first)
        flag = 1
    else:
        first = arr[0]
        arr.remove(first)
        s.append(first)
        flag=1
while len(arr) != 0:
    if flag:
        mx = max(arr[0], arr[-1])
        d.append(mx)
        arr.remove(mx)
        mx2 = max(arr[0], arr[-1])
        s.append(mx2)
        arr.remove(mx2)
    else:
        mx = max(arr[0], arr[-1])
        s.append(mx)
        arr.remove(mx)
        mx2 = max(arr[0], arr[-1])
        d.append(mx2)
        arr.remove(mx2)

print(sum(s), sum(d))


