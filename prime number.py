def isprime(x):
    y = True
    for i in range(2, x):
        if i % 2 == 0:
            y = False
        elif i == 1:
            y = False
    return y


print(isprime(1))
