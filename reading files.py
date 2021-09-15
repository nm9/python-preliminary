# different file access modes r - read,w - write,r+ - read & write,a - append

employee_file = open("dealing with files/employees.txt", "r")

is_readable = employee_file.readable()
if is_readable:
    print(is_readable)
    # print(employee_file.read())                #read full file

    # print(employee_file.readline())            #read 1st line in file
    # print(employee_file.readline())            #read 2nd line in file

    # print(employee_file.readlines())           #read all lines in file and o/p in form of a list/array
    # read 2nd element of list/array formed above
    print(employee_file.readlines()[1])

employee_file.close()

employee_file = open("reading files/employees.txt", "r")

is_readable = employee_file.readable()
if is_readable:
    for employee in employee_file.readlines():
        print(employee)

employee_file.close()
