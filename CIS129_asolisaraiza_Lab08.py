"""Palindrome Tester"""
#Angel Solis
#CIS129 Lab08
#4/6/2024


def main():
    state = "continue"
    while state == "continue":
        print("Welcome to the Palindrome tester! Give you word to check it")
        ispalindrome()
        #Loop phase
        while True:
            try:
                answer = input("Do you want to coninue testing more words/senteces? (Yes/No)\n")
                if answer.lower() == "y" or answer.lower() == "yes":
                    state = "continue"
                    break
                if answer.lower() == "n" or answer.lower() == "no":
                    state = "end"
                    break
                else:
                    print("Please answer")
            except ValueError:
                   print("Error data")

def ispalindrome():
        word = input("Here:")
        #Function in charge to filter the whole string no matter punctuation
        wordcheck = "".join(letter for letter in word if letter.isalnum()).lower()
        #Results
        print("In rough terms you word/sentece is:",
              "\n Normal:", wordcheck,
              "\n Reverse:",wordcheck[::-1])
        if wordcheck == wordcheck[::-1]:
            print(word, "is a palindrome!")
        else:
            print(word, "is not a palindrome")

main()
