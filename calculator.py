n1 = float(input('Enter first number: '))
op = input('Enter operator (Choose from +,-,*,/,%,pow) \n')
n2 = float(input('Enter second number: '))

if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '*':
    result = n1 * n2
elif op == '/':
    result = n1 / n2
elif op == '%':
    result = n1 % n2
elif op == 'pow':
    result = pow(n1, n2)
else:
    print('invalid operator')

print(result)