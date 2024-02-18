#CIS129 Lab04
#Angel Solis
#Module 4 Lab Part2



#It will prompt to the user the monthly sales and its increase
# and get the results for the specifications asked for.
#Define variables
storeAmount = 0
empAmount = 0
salesIncrease = 0 
monthlySales = 0

#Getting monthly sales
monthlySales = float(input('Enter mointhly sales $'))
if monthlySales > 110000:
    storeAmount=6000
elif monthlySales >= 110000:
     storeAmount=5000
elif monthlySales >= 90000:
     storeAmount=4000
elif monthlySales >= 80000:
    storeAmount=3000
else:
    storeAmount=0
#Getting store sales increase
salesIncrease=float(input('Enter percent of sales increase: '))
salesIncrease= salesIncrease/100
if salesIncrease>=.05:
    empAmount= 75
elif salesIncrease >=0.04:
    empAmount= 50
elif salesIncrease >= 0.03:
    empAmount=40
else:
    empAmount=0
print("The store bonus amount is $"+str(storeAmount)+"")
print("The employee bonus amount is $"+str(empAmount)+"")
if storeAmount == 6000 and empAmount== 75:
    print("Congrats! You have reached the highest bonus amounts possible!\n\
          Now you are mafia boss")
          
