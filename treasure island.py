print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/"=._o--._        ; | ;        ; ;/______/______/_______/
/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/_______/
/______/______/______/_____"=._o._; | ;_.--"o.--"_/______/______/______/_____/
/______/______/______/______/__"=.o|o_.--""___/______/______/______/______/__
*******************************************************************************
''')



print("welcome to the treasure island")
print("your mission is to find the treasure")
direction=input("where do you want to go? left or right   ").lower()
if direction=="left":
   swim=input("do you want to swim of wait for the boat ?  type  'swim ' to swim acroos the river or  type 'wait'  to wait for the magical boat ").lower()
   print(swim)
   if swim=="wait":
       color=input("which door do you want to use? red  or blue or yellow ?  ").lower()
       print(color)
       if color=="red":
           print(" you enter a room full of fire.Game Over")
       elif color=="blue":
           print(" you enter  room full of zombies.Game Over")
       elif color=="yellow":
           print(" you have ntered the treasure room.you win!!!!!!!!!")
            
   else:
       print("  You were eaten by sharks .Game OVer")
       
else:
    print("Game Over")