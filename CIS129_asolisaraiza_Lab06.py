""" Hotdog Cookout autocounter"""

#Angel Solis
#CIS129 Lab06
#03/12/2024

#For getting the correct amount of packages
import math

def main():
    total=getTotalHotDogs()
    DOGS=10
    BUNS=8
    dogsLeft=0
    bunseLeft=0
    minDogs=0
    minBuns=0
    #Operation charge of the sorting and leftovers
    minDogs = math.ceil(total/DOGS)
    dogsLeft = (DOGS - (total%DOGS))%DOGS
    bunsLeft = (BUNS - (total%BUNS))%BUNS
    minBuns= math.ceil(total/BUNS)
    #Self-explanatory
    Showresults(minDogs, minBuns,bunsLeft,dogsLeft)

def getTotalHotDogs():
#Input validation for getting integer
    while True:
        try:
            people=int(input("Enter the number of people attending the cookout: "))
            hotDogs=int(input("Enter the number of hotdogs attending\
    for each person: "))
            #Operation
            total = people * hotDogs
            return total
        except ValueError:
            print("An integer please")

def Showresults(minDogs,minBuns,bunsLeft,dogsLeft):
    print("Minimum packages of hot dogs needed: ", minDogs)
    print("Mininum packages of hot dog buns needed: ", minBuns)
    print("Hot dog left over: ", dogsLeft)
    print("Hot dog buns left over: ", bunsLeft)

main()
