import random
print("Hello I am Aklil Zewde ☺ \n Rock Paper Scissor Game")
while True:
    player_choice = input(
        "Enter a choice(0 for Rock, 1 for paper, 2 for scissor):")
    choice = int(player_choice)
    computer_choice = random.randint(0, 2)
    players_choice_string = " "
    computer_choice_string = " "

    if choice == 0:
        players_choice_string = "rock"
    elif choice == 1:
        players_choice_string = "paper"
    elif choice == 2:
        players_choice_string = "scissor"
    else:
        players_choice_string = "please enter the correct input"

    print(f"\n Your choice {players_choice_string}")

    if computer_choice == 0:
        computer_choice_string = "rock"
    elif computer_choice == 1:
        computer_choice_string = "paper"
    else:
        computer_choice_string = "scissor"

    print(
        " Your choice  is ", players_choice_string)
    print("computer choice is", computer_choice_string)
    print(computer_choice_string, "vs", players_choice_string)

    if choice == computer_choice:
        print(f"Both players selected {players_choice_string}. No winner ")
    elif choice == 0:
        if computer_choice == 2:
            print("Congragulation you win.................Rock breaks scissor   ")
        else:
            print("Sorry you lose...........paper covers rock")
    elif choice == 1:
        if computer_choice == 0:
            print("Congradulation You win...........Paper covers rock")
        else:
            print("Soory you lose.................Scissors cuts paper!")
    elif choice == 2:
        if computer_choice == 1:
            print("congradulation You win...............Scissors cut paper")
        else:
            print("Sorry you lose..................Rock breaks scissors")

    repeat_game = input("do you want to play again? (y/n):")
    if repeat_game.lower() != "y":
        break
