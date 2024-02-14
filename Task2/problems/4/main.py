N = int(input())
arr = []
for i in range(N):
    # taking the input as a list.
    method = list(input().split())
    if method[0] == "print":
        print(arr)
    elif method[0] == "remove":
        if int(method[1]) in arr:
            arr.remove(int(method[1]))
    elif method[0] == "insert":
        arr.insert(int(method[1]), int(method[2]))
    elif method[0] == "append":
        num = int(method[1])
        arr.append(num)
    elif method[0] == "sort":
        arr.sort()
    elif method[0] == "pop":
        arr.pop()
    elif method[0] == "reverse":
        arr.reverse()

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print









