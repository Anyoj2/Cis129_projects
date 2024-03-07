""""" Exercises 3.1"""
#Angel Solis
#CIS129 Mod05 assignment
#03/06/2024


#Modification of fig.3.3
# initialize variables
passes = 0
failures = 0  
counter=0
# process 10 students
while counter !=10:
    # get one exam result
    result = input('Enter result (1=pass, 2=fail): ')
    try:
        result = int(result)
        if result == 1:
            passes += 1
            counter+=1
        elif result==2:
            failures += 1
            counter+=1
        else:
            print("Error, try 1 or 2.")  
    except ValueError:
        print('An integer please.')

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
