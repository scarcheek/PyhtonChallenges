# a=1  b=2  c=3  ->  maximum=3
# a=1  b=3  c=2  ->  maximum=3
# a=1  b=1  c=3  ->  maximum=3
# a=1  b=1  c=1  ->  maximum=1

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if (a > b and a > c):
    maximum = a

if (b > a and b > c):
    maximum = b

if (c > a and b > c):
    maximum = c

print('Maximum:', maximum)

