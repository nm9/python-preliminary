is_male=False
a=0

if is_male:
    print('You are a male')
    a=a+1
else:
    print('You are a female')
    a=a+2

print(a)

is_tall=False

if is_male or is_tall:
    print('male or tall')

if is_male and is_tall:
    print('male and tall')
elif is_male and not is_tall:
    print('male not tall')
elif is_tall and not is_male:
    print('tall not male')
else:
    print('shit')


def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(2,3,500))