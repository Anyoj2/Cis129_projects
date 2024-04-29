"""Check protection"""
#Angel Solis
#CIS129 Lab10
#04/23/2024

def printCheck(userCheck):
    Check = f'{userCheck:10,.2f}'
    print("Your check is the amount of\n",Check.replace(" ","*"))
def main():
    state = "continue" 
    print("Welcome to the Chech Potection Program. Give your check amount numeric value:")
    while state == "continue":
        try:
            userCheck = float(input("Here:"))
            
            while len(str(userCheck)) > 10:
                print("Too large")
                userCheck = float(input("Here:"))
                
            if userCheck == 0:
                print("**********")
            else:
                printCheck(userCheck)
                
            while True:
                answer = input("Do you want to check another amount? (Yes/No)\n")
                if answer.lower() == "y" or answer.lower() == "yes":
                    state = "continue"
                    break
                if answer.lower() == "n" or answer.lower() == "no":
                    state = "end"
                    break
                else:
                    print("Please answer")
        except ValueError:
            print("A number please")


main()

    

