list1 = []                              # note the type of brackets
list1.append('hello')
print(list1)

tuple1 = (2, 3)  # immutable            #note the type of brackets
print(tuple1[0])

dict1 = {}                              # note the type of brackets

for k in range(1, 5):         # k=key, v=value
    dict1[k] = dict1.get(k, 0)+k

print(dict1)
