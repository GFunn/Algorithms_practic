def factorial(i):
    if i == 1:
        return 1
    else:
        return i * factorial(i - 1)


x = int(input('input: '))
print('output: %d' % factorial(x))
