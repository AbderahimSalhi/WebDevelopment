import time
import random


def print_pause(msg):

    print(msg)
    time.sleep(1)


creatures = random.choice(["troll", "pirate", "wolf", "wicked fairie",
                           "gorgon"])
items = []


def intro():
    print_pause("you find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {creatures} is somewhere around here,"
                " and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                " dagger.\n")


def prompt():

    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause("What would you like to do?")
    print_pause("(Please enter 1 or 2).")


def place_choice():
    # Input validation for place choice
    select = input()
    if select == "1":
        house()
    elif select == "2":
        cave()
    else:
        print("Please enter 1 or 2")
        place_choice()


def replay():
    # Whether the player want to play again or quit with input validation
    answer = input()
    if answer == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif answer == "n":
        print("Thanks for playing! See you next time.")
    else:
        print_pause("Would you like to play again? (y/n)")
        replay()


def fight():
    # Things that happen when the player fights
    if "sword" in items:
        print_pause(f"As the {creatures} moves to attack, you unsheath"
                    " your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand"
                    " as you brace yourself for the attack.")
        print_pause(f"But the {creatures} takes one look at your shiny"
                    " new toy and runs away!")
        print_pause(f"You have rid the town of the {creatures}."
                    " You are victorious!")
        print_pause("Would you like to play again? (y/n)")
        replay()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the gorgon.")
        print_pause("You have been defeated!")
        print_pause("Would you like to play again? (y/n)")
        replay()


def cave():
    # Things that happen to the player goes in the cave
    print_pause("You peer cautiously into the cave.")
    if "sword" not in items:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take"
                    " the sword with you.")
        print_pause("You walk back out to the field.\n")
        items.append("sword")
        prompt()
        place_choice()
    else:
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        prompt()
        place_choice()


def field():
    # Things that happen when the player runs back to the field

    print_pause("You run back into the field. Luckily, you don't"
                " seem to have been followed.")
    prompt()
    place_choice()


def fight_run():
    # Run or Fight with input validation
    choice = input()
    if choice == "1":
        fight()
    elif choice == "2":
        field()
    else:
        print("Please enter 1 or 2")
        fight_run()


def house():
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and"
                f" out steps a {creatures}.")
    print_pause(f"Eep! This is the {creatures}'s house!")
    print_pause(f"The {creatures} attacks you!")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this, what"
                    " with only having a tiny dagger.\n")
    print_pause("Would you like to (1) fight or (2) run away?")
    fight_run()


def play_game():
    intro()
    prompt()
    place_choice()


play_game()
