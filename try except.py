##try except

#number = int(input('Enter a number: '))
#print(number)                                  this is the normal program

check=0
while check<1:
    try:
        #value=10/0
        number = float(input('Enter a number: '))
        print(number)
        check+=1
    except ZeroDivisionError as err:
        print(err)
        check+=1
        #quit()                                                 #if further code is present, which will usually be the case, quit ensures it doesnt execute and you do not get a traceback from there
    except ValueError as er2:
        print("Invalid input. " + str(er2))                      #this ensures program doesnt throw up error even if input isnt a number