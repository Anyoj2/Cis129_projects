"""A try of rpg. Dude wants to go to the beach and gets struck by monsters\
in the way"""

#Angel Solis
#Start date 2/14/2024 coursing CIS129
#Just for fun
#Currently 0.2.1 for now. No real depth in the number


print("On a shiny day in the woods of a lonely isle, the Beachdude wanted\
 to just spend in shrine all day long enjoying the ocean. \
 However, some monsters get in the way!")

#Setting base stats of first battle----------------------------------------

NameMonster="Horned Cow"
print(NameMonster)
Monsterhealth=100
Monsterdmg=5
Monsterarmor=0
Monsterdfs=0

Beachdude=100
Beachdudedmg=20
Beachdudearmor=0
Beachdudedfs=50

Sword=50 #Dont ask where it came from
ArmorDude=25 #Same for all
Potion= 50
Greatsword= 100
ultragreatsword=200

itemgreatsword=0
itemsword=0
itempotion=0
itemarmor=0
itemultragreatsword=0
victory=0
#Battle system?----------------------------------------------------------------

Currenthealth= Beachdude - Monsterdmg
Monstercurrenthp =  Monsterhealth - Beachdudedmg


print("A big "+str(NameMonster)+"  with servere gigantism appears hitting you")
print("Now you have " +str(Currenthealth)+"hp\n\
Press E to Exit or can check you inventory and stats by pressing I. \n Attack/Defend (Write A or D)")

while True:

    if Currenthealth == 0:
        print("\n \n Everything starts to fade in black...")
        break
    print("Press E to Exit. Can check you inventory and stats by pressing I. \n    Attack/Defend (Write A or D)")
    action=input()
    if action.lower()=="e":
        print("End")
        break
    if action.lower()== "a" and Monstercurrenthp > 0 :
        print("Give it an overhand! Deals "+str(Beachdudedmg)+" Now\
 the cow has "+str(Monstercurrenthp)+"hp")
        Monstercurrenthp -= Beachdudedmg
        Currenthealth -= Monsterdmg
        print("Strikes back the "+str(NameMonster)+"! Dealing "+str(Monsterdmg)+"dmg. Now you have "+str(Currenthealth)+"hp.\n\
Attack/Defend (Write A or D)")
    elif action.lower()=="d" and Beachdude > 0:
        Currenthealth -= Monsterdmg/(100/Beachdudedfs)
        print("Straighten your arms together."+str(NameMonster)+" dealing "+str(Monsterdmg)+"dmg. Now you have "+str(Currenthealth)+"hp\n\
Attack/Defend (Write A or D)")
    elif action.lower() == "i":
        print("You check you inventory and you have:")
        if itemgreatsword >= 1:
            print("A formidable greatsword " + str(itemgreatsword) + "")
        if itemsword >= 1:
            print("A common sword")
        if itempotion >= 1:
            print("A red flask")
        if itemarmor == 1:
            print("The vest on")
        if itemultragreatsword >= 1:
            print("An enormous sword which you should consider a gift")

        print("Health:", Currenthealth)
        print("Damage:", Beachdudedmg)
        print("Armor:", Beachdudearmor)
    elif Monstercurrenthp==0:
        print("...And the cow fall back... Cow. Dead. Continue. Beach")
        victory +=1
        break
    else:
        print("Invalid action")


#Random sys arrives------------------------------------------------------
import random
#Item list and dmg/value
#Dont ask where the items came from
#Same for all
Sword=50
ArmorDude=25
Potion= 50
Greatsword= 100
ultragreatsword=200

itemgreatsword=0
itemsword=0
itempotion=0
itemarmor=0
itemultragreatsword=0
#Chest time------------------------------------------------------
if victory >= 1:
    print("A chest, Would you like to check w-\n You open it")
    for roll in range(1):
            face = random.randrange(1,100)
    if face > 0 and face <= 40:
        itemsword +=1
    if itemsword==1:
        print("A sword, very practical for today")

    if face >90 and face <=98:
        itemarmor += 1
        print("A vest to reduce some hit")
    if face >40 and face <=70:
        itempotion +=1
        print('A flask filled with blood (A potion)')
    if face > 70 and face<=90:
        itemgreatsword +=1
        print("Nice one, a doubled handled sword")
    if face ==1:
        itemultragreatsword +=1
        print("Well, you got it, the 1%. Enjoy the dmg")

if itemsword==1:
    Beachdudedmg += Sword
if itemarmor == 1:
    Beachdudearmor += ArmorDude
if itemgreatsword==1:
    Beachdudedmg  += Greatsword
if itemultragreatsword==1:
    Beachdudedmg += ultragreatsword
    
#Itembag and stats---------------------------------------------------------------------
if action.lower()=="i":
    print("You check you inventory and you have:")
    if itemgreatsword >=1:
        print("A formidable greatsword "+str(itemgreatsword)+"")
    if itemsword >=1:
        print("A common sword")
    if itempotion >=1:
        print("A red flask")
    if itemarmor == 1:
        print("The vest on")
    if itemultragreatsword >=1:
        print("An enormous sword which you should consider a gift")

    print("Health:", Currenthealth)
    print("Damage:", Beachdudedmg)
    print("Armor:",Beachdudearmor)
#battle2----------------------------------------------------------------
NameMonster=str("Goblino")
Monsterhealth=150
Monsterdmg=10
Monsterarmor=0
Monsterdfs=0
#Preface battle2--------
while True:
    if victory == 1:
        print("Continue? (Yes/No)")
        answer = input("Answer:")
    elif victory == 0:
        break
    if answer.lower() == "yes":
        print("Keep track of my mission")
        break
    if answer.lower() == "no":
        victory -= 1
        print("Sure")
        break
    else:
        print("Dont be shy, lets go again")
if victory>=1:
    #Battle system2-----------------------------------------------------------------------------------
    Monstercurrenthp = Monsterhealth
    print("\n\n\n")
    print("A "+str(NameMonster)+" with a twisted smile appears")
    print("You have " +str(Currenthealth)+"hp\n\
    Press E to Exit)")
    while True:

        print("Attack/Defend (Write A or D)")
        action=input()
        if action.lower() == "a":
            Monstercurrenthp -= Beachdudedmg
            if Monstercurrenthp < 0:
                Monstercurrenthp = 0
            print("Strike it dealing "+str(Beachdudedmg)+"dmg. Now "+str(NameMonster)+" has "+str(Monstercurrenthp)+"hp.")
            if Monstercurrenthp <0 or Monstercurrenthp == 0:
                print("The "+str(NameMonster)+" has fallen down.")
                victory += 1
                break
            elif Monsterhealth > 0:
                Currenthealth -= Monsterdmg - (Monsterdmg*(Beachdudearmor/100))
                print("The "+str(NameMonster)+" hits back dealing" +str(Monsterdmg)+"dmg. You have "+str(Currenthealth)+"hp.")
        if action.lower() == "d":
            if action.lower()=="d" and Currenthealth > 0:
                Currenthealth -= Monsterdmg/(100/Beachdudedfs) - (Monsterdmg*(Beachdudearmor/(100)))
                print("Straighten your arms together."+str(NameMonster)+" dealing "+str(Monsterdmg)+"dmg.\
                 Now you have "+str(Currenthealth)+"hp\n")
        if action.lower()=="p" and itempotion >=1:
            Currenthealth += Potion
            print("used the flask, restored some health and now "+str(Currenthealth)+"hp")

        if Currenthealth<=0:
            print("you ded")
            break
        elif action.lower() == "i":
            print("You check you inventory and you have:")
            if itemgreatsword >= 1:
                print("A formidable greatsword " + str(itemgreatsword) + "")
            if itemsword >= 1:
                print("A common sword")
            if itempotion >= 1:
                print("A red flask")
            if itemarmor == 1:
                print("The vest on")
            if itemultragreatsword >= 1:
                print("An enormous sword which you should consider a gift")

            print("Health:", Currenthealth)
            print("Damage:", Beachdudedmg)
            print("Armor:", Beachdudearmor)
        elif action.lower() == "e":
            print("End")
            break
        else:
            print("Invalid action")
#Chest time 2-------------------------------------------------------------------------
    if victory >= 2:
        print("A chest, Would you like to check w-\n You open it")
        for roll in range(1):
            face = random.randrange(1, 100)
        if face > 0 and face <= 40:
            itemsword += 1
        if itemsword == 1:
            print("A sword, very practical for today")

        if face > 90 and face <= 98:
            itemarmor += 1
            print("A vest to reduce some hit")
        if face > 40 and face <= 70:
            itempotion += 1
            print('A flask filled with blood (A potion)')
        if face > 70 and face <= 90:
            itemgreatsword += 1
            print("Nice one, a doubled handled sword")
        if face == 1:
            itemultragreatsword += 1
            print("Well, you got it, the 1%. Enjoy the dmg")

    if itemsword == 1:
        Beachdudedmg += Sword
    if itemarmor == 1:
        Beachdudearmor += ArmorDude
    if itemgreatsword == 1:
        Beachdudedmg += Greatsword
    if itemultragreatsword == 1:
        Beachdudedmg += ultragreatsword
    #End phase for now--------------------------------------------------------------
    while True:
        if victory==2:
            print("Continue? (Yes/No)")
            answer=input("Answer:")
        elif victory==0:
            break
        if answer.lower() == "yes":
            print("Na huh")
            answer=input(" respond me:")
            print("dont care bye")
            break
        if answer.lower() == "no":
            print("ok")
            break
        else:
            print("Dont be shy, lets go again")







      




      
