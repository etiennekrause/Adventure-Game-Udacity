import time
import random


def print_pause(message, delay=1):
    print.sleep(delay)
    print(message)
    time.sleep(1)


def intro(item, option):
    print_pause("You find yourself standing in an open field,",
             "filled with grass and yellow wildflowers.\n", 3)
    print_pause("Rumor has it that a " + option + " is somewhere "
             "around here, and has been terrifying the nearby village.\n", 3)
    print_pause("On the right side you see an old, abandoned cave "
             "from which mystical sounds are coming.\n", 3)
    print_pause("In front of you, you see an old overgrown house. "
             "The roof has already collapsed.\n"
             "Only the entrance seems to be in order.\n", 3)
    print_pause("In your left hand you hold a dirty wooden stick, "
             "which you found in the forrest.\n", 3)
    print_pause("Not really helpful.\n", 3)


def house(item, option):
    print_pause("\nYou chose the house option.\n", 2)
    print_pause("You walk towards the entrence of the house.", 2)
    print_pause("You knock on the door.", 2)
    print_pause("Suddenly, a " + option + " opens the door.", 2)
    print_pause("Oh no, what should we do?!", 2)
    if "laser sword" not in item:
        print_pause("You don't feel well prepared for this.", 2)
    while True:
        choice2 = input("Would you like to fight (1) or run away (2)?\n")
        if choice2 == "1":
            if "laser sword" in item:
                print_pause("\n The " + option + " attacks you!\n", 2)
                print_pause("That will be a tough fight, go for it!", 2)
                print_pause("You take your laser sword and try to "
                         "defend yourself.", 2)
                print_pause("However, the " + option + " gets afraid...", 2)
                print_pause("...and runs away!", 2)
                print_pause("What a victory for you!", 2)
                print_pause("Congratulations! You made it!", 2)
                print_pause("Finally, the people in the village doesn't "
                         "need to be afraid anymore.", 2)
            else:
                print_pause("\nYou really tried your best...!", 2)
                print_pause("However, your wooden stick was not good "
                         "enough.", 2)
                print_pause("You've unfortunately lost against "
                         "the " + option + ".", 2)
            play_another_round()
            break
        if choice2 == "2":
            print_pause("\nThat was a good choice.", 2)
            print_pause("You run away and try to find something else.\n", 2)
            choice(item, option)
            break


def cave(item, option):
    if "laser sword" in item:
        print_pause("\nYou chose the cave option.\n", 2)
        print_pause("You go slowly into the cave, but it's very dark.", 2)
        print_pause("You remember that you've been here before.", 2)
        print_pause("There is nothing else in here.", 2)
        print_pause("You walk back.\n", 2)
    else:
        print_pause("\nYou chose the cave option.\n", 2)
        print_pause("You go slowly into the cave, but it's very dark.", 2)
        print_pause("Suddenly, you hear a buzzing sound.", 2)
        print_pause("As you get closer, the light gets brighter and brighter.", 2)
        print_pause("You can't believe it.", 3)
        print_pause("...silence...", 3)
        print_pause("You found a laser sword from Star Wars!!", 3)
        print_pause("You throw away the wooden stick and take the laser sword.", 2)
        print_pause("You walk back.\n", 2)
        item.append("laser sword")
    choice(item, option)


def choice(item, option):
    print_pause("Enter 1 to knock on the door of the house.", 1)
    print_pause("Enter 2 to peer into the cave. ", 1)
    print_pause("What would you like to do?", 1)
    while True:
        choice1 = input("(Please enter 1 or 2).\n")
        if choice1 == "1":
            house(item, option)
            break
        elif choice1 == "2":
            cave(item, option)
            break


def play_another_round():
    next_round = input("Would you like to play again? (y/n)\n").lower()
    if next_round == "y":
        print_pause("Cool, let's play again..!\n\n", 1)
        play_game()
    elif next_round == "n":
        print_pause("\n\nThanks for playing the game. See you soon!\n\n", 1)
    else:
        play_another_round()


def play_game():
    item = []
    option = random.choice(["pirate", "monster", "thief"])
    intro(item, option)
    choice(item, option)


play_game()
