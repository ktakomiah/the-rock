print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
if height >= 120:
    print("you can go on  the rollrcoaster")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("please pay $5")
    elif age <= 18:
        bill = 7
        print("give the $7 ticket")
    else:
     bill = 12
    print("give her the $12 ticket")
    
    
    
    want_photo = input("do you want a pic? type Y or N? ")
    # Additional logic for want_photo can be added here
    if want_photo=="Y":
     bill+=3
     print(f"your final bill is {bill}")
else:
 print("you cannot ride ,wait for next year")
# if want_photo=="3"
# print ("welcome to my humble abode")
# number=int(input("choose a number from one to ten  "))
# if number%2==0:
    # print("the number is an even number")
# else:
    # print ("the number is and odd number")