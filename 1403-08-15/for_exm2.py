userenter = int(input("enter number : ")) # 5


if userenter != 0 :
    numbers = range(1 , userenter+1) # [1,2,3,4,5,6]
    for i in numbers:
        print(i)
else:
    print('zero')



