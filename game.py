import random


name = input("What is your name? ")


print("Good Luck ! ", name)

words = ["v"]


word = random.choice(words)


print("Guess the letter")

guesses = ''


turns = 7


while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char)

        else:
            print("_")

            
            failed += 1

    if failed == 0:

        print("WINNER")


        print("The word is: ", word)
        break


    guess = input("guess a character:")

  
    guesses += guess

    
    if guess not in word:

        turns -= 1


        print("Wrong")

        print("You have", + turns, 'more trys')

        if turns == 0:
            print("Game Over")
vito