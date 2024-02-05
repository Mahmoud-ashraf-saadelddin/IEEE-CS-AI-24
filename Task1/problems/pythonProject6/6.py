x = int(input())
sum =0
if x > 0 :
    for i in range(0, x + 1, 2):
        sum += i
    print(f"The sum of even numbers from 1 to {x} is {sum}")
