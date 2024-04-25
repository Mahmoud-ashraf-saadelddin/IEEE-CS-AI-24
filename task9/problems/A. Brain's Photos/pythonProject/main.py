n,m = map(int,input().split())
arr=[]
c=0
for i in range(n):
    arr.append(list(input().split()))
    for j in arr[i]:
        if j =='C' or j == 'M' or j=='Y':
            c+=1
if c > 0:
    print("#Color")
else:
    print("#Black&White")


