a = input()
b = input()
c = input()

if a.isdigit():
    x = int(a)+3
if b.isdigit():
    x = int(b)+2
if c.isdigit():
    x = int(c)+1

if x%5 == 0 and x%3 == 0:
    print('FizzBuzz')
elif x%3 == 0:
    print('Fizz')
elif x%5 == 0:
    print('Buzz')
else:
    print(x)