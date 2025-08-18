import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

result = 1
for n in range(1, 21):
    result = lcm(result, n)

print(result) 