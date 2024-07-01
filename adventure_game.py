import random
import time


def print_by_time(message, waiting_time):
    print(message)
    time.sleep(waiting_time)


def intro():
    print_by_time("You are now in front of the entrance to a large zoo.", 2)
    print_by_time(f"There was a report of an {animal} causing problems.", 2)
    print_by_time("and concerns to people here.", 2)
    print_by_time("In front of you is the house of the cheetah.", 2)
    print_by_time("To your right is a house of snakes.", 2)
    print_by_time(f"In your hand you hold a {tools}.", 2)


def facing(animal):
    print_by_time(f"{animal} is approaching you!", 1)
    if tools == "Phone camera":
        print_by_time("You feel like you're not very prepared for this.", 2)
        print_by_time(f"with only {tools}.", 2)
    selection = ''
    while selection != '1' or selection != '2':
        selection = input("Do you want to (1) approach or (2) run away? \n")
        if selection == '1':
            if tools == "Phone camera":
                print_by_time("You do your best..", 2)
                print_by_time(f"But your {tools} can't confront {animal}.", 2)
                print_by_time("You lost in the confrontation!", 3)
            elif tools == "tranquilizer gun":
                print_by_time("You ready your tranquilizer gun", 2)
                print_by_time(f"The {animal}calms down when handled", 2)
                print_by_time(f"You managed to control the {animal}.", 2)
                print_by_time("You are victorious!", 2)
        elif selection == '2':
            print_by_time("You are now on the way to the main path.", 2)
            print_by_time("Fortunately he didn't catch you.", 2)
            where_to_now()
        else:
            print_by_time("Input Error!, Please re-enter", 2)


def where_to_now():
    print_by_time("Enter 1 to visit the Cheetah House.", 2)
    print_by_time("Enter 2 to visit and explore the House of Snakes.", 2)
    selection = ''
    while selection != '1' or selection != '2':
        selection = input("# Please Enter 1 or 2 # \n")

        if selection == '1':
            cheetah_house()
        elif selection == '2':
            house_of_snakes()
        else:
            print_by_time("Input Error!, Please re-enter", 2)


def cheetah_house():
    print_by_time("You are now moving forward.", 2)
    print_by_time("and approaching the cheetah's house.", 2)
    print_by_time(f"{animal} suddenly appears in front of you.", 2)
    facing(animal)


def house_of_snakes():
    global house_of_snakes_visited
    global tools
    print_by_time("You enter the snake house with caution.", 2)
    if house_of_snakes_visited:
        print_by_time("It is now just an empty container.", 2)
    else:
        print_by_time("There is a sleeping gun for animals", 2)
        print_by_time(f"You ditch your {tools}.", 2)
        print_by_time("and grab the tranquilizer gun.", 2)
        tools = "tranquilizer gun"
        house_of_snakes_visited = True
    print_by_time("You can return to the main path of the zoo.", 3)
    where_to_now()


def play_again():
    selection = input("Would you like to play again? (yes // no) \n")
    if selection == 'no':
        print_by_time("Thank you for nice playing ! See you later", 3)
        return 'Game_Over'
    elif selection == 'yes':
        print_by_time("Restarting the game ....", 3)
        return 'run'


game_state = 'run'
while game_state != 'Game_Over':

    animals = ['tiger', 'monkey', 'alligator', 'giraffe', 'elephant']
    animal = random.choice(animals)
    tools = 'Phone camera'
    house_of_snakes_visited = False

    intro()
    where_to_now()

    game_state = play_again()
