# gcd as known as Greatest Common Divisor
def gcd(a, b):
    if a <= 0 or b <= 0:
        print('need positive integer')
        return
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


a = int(input('input a: '))
b = int(input('input b: '))
print(gcd(a, b))
