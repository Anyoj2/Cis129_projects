"""A try of rpg. Dude wants to go to the beach and gets struck by monster\
in the way"""

#Angel Solis
#Start date 2/14/2024 coursing CIS129
#Just for fun

print("On a shiny day in shrine of a lonely, the Beachdude wanted\
 to just spend all day long in the ocean. \
 However, some monsters get in the way!")
#Setting base stats of first battle
Monster1health=100
Monster1dmg=5
Monster1armor=0
Monsterdfs=0

Beachdude=100
Beachdudedmg=20
Beachdudearmor=0
Beachdudedfs=50

#Battle system?

Currenthealth= Beachdude - Monster1dmg
Monster1currenthp =  Monster1health - Beachdudedmg


print("A big horned cow with servere gigantism appears hitting you")
print("Now you have " +str(Currenthealth)+"hp\n\
Attack/Defend (Write A or D)")

while True:
    if Currenthealth == 0:
        print("\n \n Everything starts to fade in black...")
        break
    action=input()
    if action.lower()== "a" and Monster1currenthp > 0 :
        print("Give it an overhand! Deals "+str(Beachdudedmg)+" Now\
 the cow has "+str(Monster1currenthp)+"hp")
        Monster1currenthp -= Beachdudedmg
        Currenthealth -= Monster1dmg
        print("Strikes back the cow! Dealing "+str(Monster1dmg)+"dmg. Now you have "+str(Currenthealth)+"hp.\n\
Attack/Defend (Write A or D)")
    elif action.lower()=="d" and Beachdude > 0:
        Currenthealth -= Monster1dmg
        print("Straighten your arms together. Cow horns dealing "+str(Monster1dmg)+"dmg. Now you have "+str(Currenthealth)+"hp\n\
Attack/Defend (Write A or D)")

    else:
        print("...And the cow fall back... Cow. Dead. Continue. Beach")
        break
        
print("A chest, Would you like to check w-\n You open it")

#Item list and dmg/value
Sword=50 #Dont ask where it came from
ArmorDude=25 #Same
Potion= 50
Greatsword= 150
ultragreatsword=200

#Random sys arrives
import random

itemgreatsword=0
itemsword=0
itempotion=0
itemarmor=0
itemultragreatsword=0

for roll in range(1):
    face=random.randrange(1,100)
if face >0 and face <=50:
        itemsword +=1
if itemsword==1:
  print("A sword, very practical for today")
    
if face >90 and face <=98:
    itemarmor += 1
    print("A vest to reduce some hit")
if face >50 and face <=90:
    itempotion +=1
    print('A flask filled with blood (A potion)')
if face ==1:
    itemultragreatsword +=1
    print("Well, you got it, the 1%. Enjoy the dmg")

while True:
    print("Continue? (Yes/No)")
    answer=input("Answer:")
    if answer.lower()== "yes":
        print("Na huh")
        answer=input(" respond me:")
        print("dont care bye")
        break
    if answer.lower()== "no":
          print("ok")
          break
    else:
        print("Dont be shy, lets go again")








      
