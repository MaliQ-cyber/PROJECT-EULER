def fibonacci_sequence():
    number = 0
    a = 1
    b = 2
    while a <= 4000000:
        if a % 2 == 0:
            number += a
        a, b = b, a + b
    return number
    
print(fibonacci_sequence())