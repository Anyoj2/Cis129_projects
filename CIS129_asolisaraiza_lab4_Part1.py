#Angel Solis
#CIS129 Lab04
#Part1

#Step 1
myAge=32
yourAge=18
myNumber=81
yourNumber=17
votingAge=18

#Step 2
if myAge == 31 and yourAge < myAge:
    print("My age is 31 and your age is less than that")
if myAge <= 35 and myAge > 32:
    print("My age is between 32 and 35")
if yourAge == votingAge or yourAge > votingAge:
    print("You can vote")
if myNumber==83 or yourNumber == 83:
    print("One of our numbers is 83")
#-----Step 3-----------------------------------------------
if myAge == 31 and yourAge < myAge:
    print("My age is 31 and your age is less than that")
else:
    print("Our ages do not qualify")
if myAge <= 35 and myAge > 32:
    print("My age is between 32 and 35")
else:
    print("My age is not within the range")
if yourAge == votingAge or yourAge > votingAge:
    print("You can vote")
else:
    print("you cannot vote")
if myNumber==83 or yourNumber == 83:
    print("One of our numbers is 83")
else:
    print("83 is not our numbers")

