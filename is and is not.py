# 'is' is equivalent to but stronger than ==, because it checks value as well as type
# for e.g.,
if 0 == 0.0:
    print('==')
if 0 is 0.0:
    print('is')
else:
    print('isn\'t equal')

var = 1
if var is not None:
    print('Not none')
