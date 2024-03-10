"""Codes from exercises 4.3, 4.4 and 4.5"""
#Angel Solis
#CIS129 Mod06 Assignment
#03/09/2024

#4.3
def cube(x):
    """Calculate the cube of x."""
    x ** 3
print('The cube of 2 is', cube(2))

#No return operator, does not work the function and gives None


#4.4
#I assume it will be a sum of squares beacuse of being 5
# 1+4+9+25=39
def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y
arg = [1,2,3,5]
print(mystery(arg))


#4.5
#The question does not ask input
# so I decided to apply two extra examples
def seconds_since_midnight(val1,val2,val3):
    hour_in_seconds = val1*3600
    minute_in_seconds = val2*60
    return hour_in_seconds+minute_in_seconds+val3
#Examples:
print("It's being since midnight",
      seconds_since_midnight(13,30,45),"seconds")
#Should be 75 more seconds
print("It's being since midnight",
      seconds_since_midnight(13,32,0),"seconds")
#proof
print("The difference:",
      seconds_since_midnight(13,32,0)-seconds_since_midnight(13,30,45))
#Should be 18067 more seconds
print("It's being since midnight",
      seconds_since_midnight(18,34,7),"seconds")
#proof
print("The difference:",
      seconds_since_midnight(18,33,7)-seconds_since_midnight(13,32,0))
