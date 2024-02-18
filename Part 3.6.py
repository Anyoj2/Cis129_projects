#Angel Solis
#Module 4 Cis129
#3.6

#Turing test
input("Welcome to a medical diagnosis. What's your problem? \nAnswer:")
answer=input("Have you have this problem before (yes or no)?\nAnswer:")
if answer.lower()=="yes":
    print("Well, you have it again")
elif answer.lower()=="no":
    print("Well you have it now")

#Would this conversation convince the user
# that the entity at the other end exhibited intelligent behavior?
# Of course not.
# Why or  why not?
#You need a massive amount of extra work on this to at least
# make it credible. Even now in days AI has a bad time responding certain
# inputs of the user. ANd it gets worse with this
# because of the instructions/design given for the program,
# being two lines of different reponse.
