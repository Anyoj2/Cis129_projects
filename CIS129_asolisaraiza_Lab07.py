"""Theater seats program"""
#Angel Solis
#CIS129 Lab07
#03/22/2024


def main():
    #Section arragnment ditributed by SEATS, PRICE and SELLS.
    A = [300,20,0]
    B = [500, 15,0]
    C = [200, 10,0]
    #Here you can add the new Section name and its values as a list.

    endProgram = "no"
    while endProgram.lower() == "no" or endProgram.lower() == "n":
        welcomeMsg(A,B,C)
        A[2], B[2], C[2] = askSells(A,B,C)
        total = incomeGenerated(A,B,C)
        displayResults(total,A,B,C)

        #Endphase
        print("Thanks for the using the program!\n")
        while True:
                endProgram=input("Do you want to close the program? (Yes or No)\n")
                if endProgram.lower() == "y" or endProgram.lower() == "yes":
                    break
                if endProgram.lower() == "n" or endProgram.lower() == "no":
                    break
                else:
                    print("Yes or No")
            

def welcomeMsg(A,B,C):
    print("Welcome to the theather!, we currenly have availiable", A[0], "seats in A section.", B[0], "seats in B section. ", C[0], "seats in C section.")

def askSells(A,B,C):
    while True:
                while True:
                    try:
                        A[2] = int(input("How many tickets sold for A section?\n"))
                        if A[2] > A[0]:
                            print("It cant be, we only have ", A[0])
                        elif A[2] < 0:
                            print("Cant be negative!")
                        else:
                            break
                    except ValueError:
                        print("An integer please")
                while True:
                    try:
                        B[2] = int(input("How many tickets sold for B section?\n"))
                        if B[2] > B[0]:
                            print("It cant be, we only have ", B[0])
                        elif B[2] < 0:
                            print("Cant be negative!")
                        else:
                            break
                    except ValueError:
                        print("An integer please")
                while True:
                    try:
                        C[2] = int(input("How many tickets sold for C section?\n"))
                        if C[2] > C[0]:
                            print("It cant be, we only have", C[0])
                        elif C[2] < 0:
                            print("Cant be negative!")
                        else:
                            break
                    except ValueError:
                        print("An integer please")

                    #Can copy-paste the while loop acordance to the new section and add it to the return. Same for other places
                    
                return A[2], B[2], C[2]

def incomeGenerated(A,B,C):
    aIncome = A[2] * A[1]
    bIncome = B[2] * B[1]
    cIncome = C[2] * C[1]
    total = aIncome + bIncome + cIncome
    return total
def displayResults(total,A,B,C):
    aLeft = A[0] - A[2]
    bLeft = B[0] - B[2]
    cLeft = C[0] - C[2]
    print("\nWe have have gathered a total of", total,"dollars with the left over of:")
    print("A section:",aLeft,"seats")
    print("B section:",bLeft,"seats")
    print("C section:",cLeft,"seats")

main()
