#the program checks the age, it can be any age you want, if it is less than what you determined it will not let the person in, if it is equal or greater it will


from time import sleep #importing the sleep library to give a certain time

print("hello user, enter your name, password and age")
name=input("enter your name: ")
sleep(1) #will wait 1 second
password=input("enter your password: ")
sleep(1) #will wait 1 second
age=int(input("enter your age: "))

if age<18:
    print("hi {}, you don't come".format(name))
if age>=18:
    print("hi  {}, you goes into".format(name))

