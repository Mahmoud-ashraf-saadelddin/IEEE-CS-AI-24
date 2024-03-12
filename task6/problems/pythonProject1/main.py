count = [0, 4, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]


def get_minimum():
    for i in range(len(count)):
        if count[i] > 0:
            return i
            break


def get_maximum():
    for i in reversed(range(len(count))):
        if count[i] > 0:
            return i
            break


def get_mean():
    length = 0
    summ = []
    for i, e in enumerate(count):
        summ.append(i * e)
        length += e
    # for i in count:
    #     if i != 0:
    #         summ.append(count.index(i)*i)
    #         length+=i
    return sum(summ) / length


# def get_array():
#     summ = []
#     for i in count:
#         if i != 0:
#             for j in range(i) :
#                 summ.append(i)
#     return summ
# new_array = get_array()
def get_median():
    mid = sum(count) / 2
    median = 0
    # odd
    if sum(count) % 2 != 0:
        total = 0
        for i in range(len(count)):
            total += count[i]
            if total >= mid:
                median = i
                return median


    #     even
    else:
        total = 0
        for i in range(len(count)):
            total += count[i]
            if total == mid:
                for k in range(i + 1, len(count)):
                    if count[k] > 0:
                        num = k
                        median = (i + k) / 2
                        return median

            elif total > mid:
                return i


def get_mode():
    return count.index(max(count))


print(get_minimum(), get_maximum(), get_mode(), get_mean(), get_median())
