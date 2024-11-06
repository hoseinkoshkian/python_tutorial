usernumber = int(input('enter number : '))

numberList = range(1,usernumber+1)

if usernumber % 2 == 0 :
    for i in numberList:
        print(i)
else :
    print('odd')