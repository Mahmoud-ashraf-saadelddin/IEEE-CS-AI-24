n = int(input())
arr = list(map(int, input().split()))
# calculate the biggest number in the list.
maximum_element = max(arr)
# count the duplication of the maximum_element in the array
count = arr.count(maximum_element)
i = 0
# removing the first maximum_element from array
while count > 0:
    arr.remove(max(arr))
    count -= 1

# printing the second maximum_element
print(max(arr))
