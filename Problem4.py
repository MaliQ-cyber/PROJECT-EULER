def pal():
    pal = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            num = a * b
            num_str = str(num)
            if num_str == num_str[::-1]:
                if num > pal:
                    pal = num
    return pal

print(pal())