def revesed_string(string):
    for i in range(len(string) - 1, -1, -1):
        return string[i]


def true_string(string):
    for x in string:
        return x


string = str(input()).strip().lower()
if true_string(string) == revesed_string(string):
    print(f"The word {string} is a palindrome.")
else:
    print(f"The word {string} is not a palindrome.")
