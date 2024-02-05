num = int(input())

#  a function that calculate divisible numbers from 2 to the user’s input number
def div_factors(num):
    nums = []
    for i in range(2,num):
        if num % i == 0:
            nums.append(i)

    return nums


#  function to check if number is prime or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


temp=[]
for i in range(len(div_factors(num))):
    if is_prime(div_factors(num)[i]):
        temp.append(div_factors(num)[i])


print(temp)
