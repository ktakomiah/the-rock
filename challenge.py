age=input(" what is your current age? ")
# born=input("what is your year of birth")
die=input("how long do you want to leave? ")
new_die=int(die)
new_age=int(age)
left=new_die-new_age
print(left)
days_left=left*366
weeks_left=left*52
month_left=left*12
print(f"you have {days_left} days,{weeks_left} weeks , and {month_left}   months left.")