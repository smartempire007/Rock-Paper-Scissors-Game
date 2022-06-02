import random


while True:

    print("\n----------------------------------------------------------")
    print("Winning Rules of the Rock paper scissor game as follows: \n"
          + "Rock vs paper->paper wins \n"
          + "Rock vs scissor->Rock wins \n"
          + "paper vs scissor->scissor wins\n"
          )

    print("---------------**************---------------\n")
    print("Rock, Paper, Scissors - Game!\n"
          + "---------------**************---------------\n")

    userChoice = input(
        'make your choice: [R] for rock🤜, [P] for paper🤚, [S] for scissors✌️ ?: ')

    if not userChoice in ['R', 'P', 'S']:
        print("Please choose a letter!")
        continue
    if userChoice != "exit":
        print("Your choice: " + userChoice)
        choices = ['R', 'P', 'S']
        Computer = random.choice(choices)
        print("Opponent choice: " + Computer)

        if Computer == str.upper(userChoice):
            print("Tie!")
        elif Computer == 'R' and userChoice.upper() == 'S':
            print("Rock beats Scissor,I win!")
            continue
        elif Computer == 'S' and userChoice.upper() == 'P':
            print("Scissor beats Paper,I win!")
            continue
        elif Computer == 'P' and userChoice.upper() == 'R':
            print("Paper beats Rock, I win!")
            continue
        else:
            print("You win!")

        Play_again = input("Play again?(Yes/No):").lower()

        if Play_again != "Yes".lower():
            break

print("Bye!")
