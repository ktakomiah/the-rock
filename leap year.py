year=input("what year do you want to check  ")
new_year=int(year)
if new_year%4==0:

    if new_year% 100!=0:
        print("it is a leap year")

    elif new_year%100==0:
      if new_year%400==0:
        print("this is  a new leap year")
      else:
          print("this is not a leap year")

    
        
else:
    print("this cannot be a leap year")