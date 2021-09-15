# None data type
smallest = None
list = [1, 2, 3]
for ele in list:
    if smallest == None:
        smallest = ele
    elif ele < smallest:
        smallest = ele

print(smallest)
