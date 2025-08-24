def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

sum = 0
number = 2

while number < 2000001:
    if is_prime(number):
        sum += number
    number += 1

print (sum)