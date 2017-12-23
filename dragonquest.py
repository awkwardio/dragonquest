from random import randint

user_hp = 5
troll_hp = 1
troll_spot = randint(0, 5)
goblin_hp = 2
goblin_spot = randint(0, 10)
dragon_hp = 3
dragon_spot = randint(0, 20)

print("Welcome to dragon's quest! Slay the evil troll, goblin, and dragon with your mighty sword! \n "
      "Guess each creature's location by picking a number. \n"
      "If you guess right, you'll hit them and take one of their HP. \n"
      "If not, the creatures will automatically hit you instead. Defeat all three and you win! \n"
      "Good luck!")

for turn in range(50):
    print("Your HP: " + str(user_hp))
    print("The troll's HP: " + str(dragon_hp))
    user_input = int(input("Pick a number between 1 and 5. "))
    if user_input != troll_spot:
        print("You missed! You lose 1 HP! Try again.")
        user_hp -= 1
        turn -= 1
        if user_hp == 0:
            print("Oh no! The troll has defeated you! Game over.")
            break
    elif user_input == troll_spot:
        print("You hit the troll and took one of his HP!")
        troll_hp -= 1
        turn -= 1
        if troll_hp == 0:
            print("Hooray! You've slain the dragon! Now you must defeat the evil goblin!")
            for turn in range(25):
                print("Your HP: " + str(user_hp))
                print("The goblin's HP: " + str(goblin_hp))
                user_input2 = int(input("Pick a number between 1 and 10. "))
                if user_input2 == goblin_spot:
                    print("You've hit the goblin! One more hit and he's dead!")
                    goblin_hp -= 1
                    turn -= 1
                    if goblin_hp == 0:
                        print("Hooray! You've defeated the goblin! Now you much slay the mighty dragon!")
                        for turn in range(10):
                            print("Your HP: " + str(user_hp))
                            print("The dragon's HP: " + str(dragon_hp))
                            user_input3 = int(input("Pick a number between 1 and 20. "))
                            if user_input3 == dragon_spot:
                                print("You hit the dragon! Keep going!")
                                dragon_hp -= 1
                                turn -= 1
                                if dragon_hp == 0:
                                    print("Hooray! You've defeated the dragon and won the game!")
                                    break
                            elif user_input3 != dragon_spot:
                                print("Oh no! The dragon has hit you!")
                                user_hp -= 1
                                turn -= 1
                                if user_hp == 0:
                                    print("Oh no! The dragon has defeated you. Game over.")
                                    break
                            else:
                                print("I'm sorry. Your input is not a choice. Please try again.")
                                turn -= 1
                elif user_input2 != goblin_spot:
                    print("Oh no! You missed and the goblin hit you!")
                    user_hp -= 1
                    turn -= 1
                    if user_hp == 0:
                        print("The goblin has defeated you! Game over.")
                        break
    elif 0 <= user_input <= 10:
        print("That's not a number between 1 and 5. Try again.")
        turn -= 1
    else:
        print("Sorry. That is not a number between 1 and 10. Try again")
        turn -= 1