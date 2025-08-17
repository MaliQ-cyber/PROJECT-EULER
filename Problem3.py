def prime_calc():
    number = 600851475143
    factor = 2
    while factor <= number:
        if number % factor == 0:
            number = number // factor
        else:
            factor += 1
    return factor

print(prime_calc())