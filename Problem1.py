numbers = list(range(1, 1000))

def find_Multiple():
    total = 0
    for i in numbers:
        if i % 3 == 0 or i % 5 ==0:
            total += i
    return total

print(find_Multiple())

