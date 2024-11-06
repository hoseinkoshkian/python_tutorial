name = input('enter name : ')
age = input('enter age : ')
phone = input('enter phone : ')

person = [ name , age , phone ]

if len(name) < 3 :
    print('not valid')
elif (int(age) < 10 or int(age)>50) :
    print("not valid ")
elif len(phone) != 3:
    print('not valid') 