#Didnt really understand this one

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

count = 0
number = 2

while True:
    if is_prime(number):
        count += 1
        if count == 10001:
            print(number)   
            break
    number += 1