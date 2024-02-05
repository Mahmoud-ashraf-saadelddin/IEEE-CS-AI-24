num = int(input())


#  a function that calculate divisible numbers from 1 to the user’s input number
def div_factors(num):
    nums = []
    for i in range(1, num):
        if num % i == 0:
            nums.append(i)

    return nums


if sum(div_factors(num)) == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
