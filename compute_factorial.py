def factorial(x):
    count = x
    while count > 1:
        x *= count - 1
        count -= 1
    return x

print factorial(0)
print factorial(1)
print factorial(2)
print factorial(3)
print factorial(4)