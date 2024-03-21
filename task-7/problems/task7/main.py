def get_probability():
    try:
        arr = list(map(int, input().split()))

    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")

    m = max(arr)
    fre_arr = [0] * (m + 1)
    for i in range(len(arr)):
        fre_arr[arr[i]] += 1

    counts = []
    for i in fre_arr:
        if i > 0:
            counts.append(i)

    for i in range(len(counts)):
        print(f" {arr[i]} : {counts[i] / len(arr)}", end=" , ")


# get_probability()
# --------------------------------------
# try:
#     event_a = list(map(int, input().split()))
#     event_b = list(map(int, input().split()))
# except ValueError:
#     print("Invalid input. Please enter only numbers separated by spaces.")
#
#
# def conditional_probability(event_a, event_b):
#     count_a = event_a.count(1)
#     count_a_and_b = 0
#
#     for i in range(len(event_a)):
#         if event_a[i] == 1 and event_b[i] == 1:
#             count_a_and_b += 1
#
#     if count_a == 0:
#         return 0  # If event A never occurs, return 0
#
#     return count_a_and_b / count_a
#
#
# print(conditional_probability(event_a, event_b))
# --------------------------------------

# prior_a = float(input())
# prior_b = float(input())
# conditional_b_given_a = float(input())
#
#
# def bayes_theorem(prior_a, prior_b, conditional_b_given_a):
#
#     return (conditional_b_given_a * prior_a) / prior_b
#
# print(bayes_theorem(prior_a, prior_b, conditional_b_given_a))
