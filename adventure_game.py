import time
import random


def print_pause(message, delay=1):
    time.sleep(delay)
    print(message)


def valid_input(item, options):
    while True:
        option = input(item).lower()
        if option in options:
            return option
        print_pause(f'Sorry, I do not understand "{option}".')


def intro(item, enemies, maps, start_weapon):
    print_pause("You find yourself standing in an open field in " + maps + ", "
                "filled with grass and yellow wildflowers.\n", 3)
    print_pause("Rumor has it that a " + enemies + " is somewhere "
                "around here, and has been terrifying the nearby "
                "village.\n", 3)
    print_pause("On the right side you see an old, abandoned cave "
                "from which mystical sounds are coming.\n", 3)
    print_pause("In front of you, you see an old overgrown house. "
                "The roof has already collapsed.\n"
                "Only the entrance seems to be in order.\n", 3)
    print_pause("In your left hand you hold a " + start_weapon + ", "
                "which you found in the forrest.\n", 3)
    print_pause("Not really helpful.\n", 3)


def house(item, enemies, maps, start_weapon):
    print_pause("\nYou chose the house option.\n", 2)
    print_pause("You walk towards the entrence of the house.", 2)
    print_pause("You knock on the door.", 2)
    print_pause("Suddenly, a " + enemies + " opens the door.", 2)
    print_pause("Oh no, what should we do?!", 2)
    if "laser sword" not in item:
        print_pause("You don't feel well prepared for this.", 2)
    while True:
        choice = valid_input("Would you like to fight (1) or run away "
                             "(2)?\n", ['1', '2'])
        if choice == "1":
            if "laser sword" in item:
                print_pause("\n The " + enemies + " attacks you!\n", 2)
                print_pause("That will be a tough fight, go for it!", 2)
                print_pause("You take your laser sword and try to "
                            "defend yourself.", 2)
                print_pause("However, the " + enemies + " gets afraid...", 2)
                print_pause("...and runs away!", 2)
                print_pause("What a victory for you!", 2)
                print_pause("Congratulations! You made it!", 2)
                print_pause("Finally, the people in the village doesn't "
                            "need to be afraid anymore.", 2)
            else:
                print_pause("\nYou really tried your best...!", 2)
                print_pause("However, your " + start_weapon + " was not good "
                            "enough.", 2)
                print_pause("You've unfortunately lost against "
                            "the " + enemies + ".", 2)
            play_another_round()
            break
        if choice == "2":
            print_pause("\nThat was a good choice.", 2)
            print_pause("You run away and try to find something else.\n", 2)
            field(item, enemies, maps, start_weapon)
            break


def cave(item, enemies, maps, start_weapon):
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
        print_pause("As you get closer, the light gets brighter and "
                    "brighter.", 2)
        print_pause("You can't believe it.", 3)
        print_pause("...silence...", 3)
        print_pause("You found a laser sword from Star Wars!!", 3)
        print_pause("You throw away the " + start_weapon + " and take "
                    " the laser sword.", 2)
        print_pause("You walk back to the field.\n", 2)
        item.append("laser sword")
    field(item, enemies, maps, start_weapon)


def field(item, enemies, maps, start_weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave. ")
    print_pause("What would you like to do?")
    while True:
        choice = valid_input("(Please enter 1 or 2).\n", ['1', '2'])
        if choice == "1":
            house(item, enemies, maps, start_weapon)
            break
        elif choice == "2":
            cave(item, enemies, maps, start_weapon)
            break


def play_another_round():
    next_round = valid_input("Would you like to play again? "
                             "(yes/no)\n", ['yes', 'no']).lower()
    if next_round == "yes":
        print_pause("Cool, let's play again..!\n\n")
        play_game()
    elif next_round == "no":
        print_pause("\n\nThanks for playing the game. See you soon!\n\n")
    else:
        play_another_round()


def play_game():
    item = []
    enemies = random.choice(["pirate", "monster", "thief"])
    maps = random.choice(["Australia", "Germany", "England"])
    start_weapon = random.choice(["wooden stick", "flashlight", "fishing rod"])
    intro(item, enemies, maps, start_weapon)
    field(item, enemies, maps, start_weapon)


play_game()
