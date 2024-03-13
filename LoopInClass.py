"""Class blank"""
#Angel Solis
#03/11/2024

def main():
    while True:
        userNum = getInteger("Give me num:")
        oddEven(userNum)
        print("Do you want to loop again")
        again=input("Press 'y' to loop again. (Anything else will break it) \n")
        if again != "y":
            break
    print('End of program')

def getInteger(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("An integer please")

def oddEven(userNum):
    if userNum%2 == 0 and userNum !=0:
        print("it's even")
    if userNum == 0:
        print("Cant say, it's zero.")
    if userNum%2==1:
        print("It's odd")
main()
