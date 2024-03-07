""" Codes of 3.3,3.4 and 3.7"""
#Angel Solis
#CIS129 Mod05 assignment
#03/06/2024

#3.3
for row in range(2):
    for col in range(7):
        print("@",end='')
    print()

#3.4
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()

#3.7
print("number square cube") 
for row in range(6):
    for col in range(3):
        print(f"{row**3:6}" if col==2 else f"{row**2:6}" if col==1 else f"{row:6}" , end="")
    print()
