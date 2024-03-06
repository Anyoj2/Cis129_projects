"""a grocery store to keep track of the total
number of bottles collected for seven days"""

#CIS lab04
#Angel Solis
#03/06/2024
#Bottle counter

#This code is not proof missbeahvior from the user
#Delcaring variables
total_bottles=0
counter=0
today_bottles=0
payout_per_bottle=0.10
keep_going="y"

#Looping process to get bottles
while keep_going=="y":
    counter+=1
    print("Enter number of bottles for day #"+str(counter)+": ", end="")
    today_bottles=int(input())
    total_bottles+=today_bottles
    total_payout=total_bottles * payout_per_bottle
#Termination phase
    if counter==7:
        print('The total number of bottles collected is',total_bottles)
        print(f"The total paid out is $ {total_payout:.1f}")
        print('Do you want to enter another week’s worth of data?\n(Enter y or n): ',end="")
        keep_going=input()
#Restart code and exit
        if keep_going=="y":
            total_bottles=0
            counter=0
            today_bottles=0
        else:
            break
