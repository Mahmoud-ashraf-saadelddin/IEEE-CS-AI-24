num = []
numbers = int(input())
num.append(numbers)
while numbers != -1:
    numbers = int(input())
    num.append(numbers)

num.remove(-1)
print(max(num))
print(min(num))
