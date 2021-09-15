list1 = ["j", "K", "l", "M", 3, False, 56.786]
##index   0     1   2   3    4    5      6
##index   -7   -6   -5  -4  -3   -2     -1
print(list1[3], list1[-3])
print(list1[1:])
print(list1[1:4])

list1[1] = "Kevin"
print(list1)


friends = ["A", "B", "C", "D", "E"]
nos = [22, 34, 51, 79, 63, 48, 190.54]
print(friends)
#friends.extend(nos)             #check out other list functions
friends.pop()
print(friends)
friends.sort()                 #only possible if list has all elements of same type, str or int or float, etc.
print(friends)
friends.reverse()
print(friends)