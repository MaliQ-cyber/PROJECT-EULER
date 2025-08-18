
def sum_square():
    numbers = list(range(1, 101))
    totalsquare = 0
    for i in numbers:
        totalsquare += i ** 2
    return totalsquare


def square_sum():
    numbers = list(range(1, 101))
    totalsum = 0
    for i in numbers:
        totalsum += i
    return totalsum ** 2

print(square_sum() - sum_square())


