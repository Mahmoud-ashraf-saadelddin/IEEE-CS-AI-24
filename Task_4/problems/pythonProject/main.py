# to calculate the length of array
def length(numbers):
    arr_length = 0
    for i in numbers:
        arr_length += 1
    return arr_length


# i will use insertion sort to sort the lists .
def insertionSort(arr):
    for i in range(1, length(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def get_numbers():
    while True:
        try:
            # Taking input from the user as a string
            input_string = input("Enter a list of numbers separated by spaces: ")

            # Splitting the input string into a list of strings
            numbers_as_strings = input_string.split()

            # Converting the list of strings to a list of floats
            numbers = [float(num) for num in numbers_as_strings]

            return numbers

        except ValueError:
            print("Error: Please enter valid numbers.")


arr = get_numbers()


def find_min(numbers):
    return insertionSort(numbers)[0]


def find_max(numbers):
    return insertionSort(numbers)[-1]


def find_mean(numbers):
    sum = 0
    for i in range(length(numbers)):
        sum += arr[i]
    return sum / length(numbers)


def find_mode(numbers):
    counts = {}
    for value in numbers:
        counts[value] = counts.get(value, 0) + 1
    max_count = max(counts.values())
    mode_values = [value for value, count in counts.items() if count == max_count]
    if len(mode_values) == 1:
        return mode_values[0]
    else:
        return "none"


def find_range(numbers):
    return insertionSort(numbers)[-1] - insertionSort(numbers)[0]


def find_median(numbers):
    # sorting the list
    numbers = insertionSort(numbers)
    if length(numbers) == 1:
        return numbers[0]
    elif length(numbers) == 2:
        return (numbers[0] + numbers[1]) / 2
    else:
        return find_median(numbers[1:-1])


#      s 2 = ∑ (x − mean)**2 / n – 1
def find_variance(numbers):
    mean = find_mean(numbers)
    sum = 0
    for i in range(length(numbers)):
        sum += (numbers[i] - mean) ** 2
    return sum / (length(numbers) - 1)  # that is the sample variance not the Population variance .


def find_STD(numbers):
    return find_variance(numbers) ** 0.5


def find_Quariles(numbers):
    Q2 = find_median(numbers)
    arr1 = []
    arr2 = []
    for i in range(1, (length(numbers) // 2) + 1):
        arr1.append(numbers[i - 1])
        arr2.append(numbers[-i])
    Q1 = find_median(arr1)
    Q3 = find_median(arr2)
    return Q1, Q2, Q3


def find_IQR(numbers):
    # order the numbers .
    insertionSort(numbers)
    arr1 = []
    arr2 = []
    # split the main array to 2 arrays .
    for i in range(1, (length(numbers) // 2) + 1):
        arr1.append(numbers[i - 1])
        arr2.append(numbers[-i])
    # calculate the median of each new array.
    Q1 = find_median(arr1)
    Q3 = find_median(arr2)
    return Q3 - Q1


print(f"Min : {find_min(arr)}")
print(f"Max : {find_max(arr)}")
print(f"Mean : {find_mean(arr)}")
print(f"Mode : {find_mode(arr)}")
print(f"Median : {find_median(arr)}")
print(f"Range : {find_range(arr)}")
print(f"Variance : {find_variance(arr)}")
print(f"Standard Deviation : {find_STD(arr)}")
print(f"Quartiles : {find_Quariles(arr)}")
print(f"Interquartile Range (IQR) : {find_IQR(arr)}")

