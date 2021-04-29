from random import randint #importing libraries
from os import system

res = -1
ten = 0

num = randint(0, 100)

while res != num:
    res = int(input("Enter a number between 0 and 100\n> "))
    if res == num:
        print("you won! :)")
    else:
        print("you missed:(")
        print(res > num and "the number is less" or "the number is higher")
        system("pause")
        system("cls")
        ten+=1

print("Answer: [{}]\nYou got it right in {} attempts".format(res, ten+1))


