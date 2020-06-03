import sys
from room import Room
from player import Player
from item import Item




# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Declare items
items = {
    'torch': Item("Torch", "Ripped rags wrapped a round a stick, to light a fire with."),
    'knife': Item("Knife", "Your trusty knife, used in all of your adventures."),
    'gold' : Item("Treasure", "A treasure chest of golden coins." ),
    'rocks': Item("Rocks", "A small cluster of smooth rocks for throwing.")
}

#Link Items to room
room['outside'].addItem(items['torch'])
room['outside'].addItem(items['knife'])
room['treasure'].addItem(items['gold'])
room['overlook'].addItem(items['rocks'])

# Main

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def start_game():
    #User Inputs name
    username = input('Enter Name To Start Your Quest: ')
    #create player instance with inputted user name and current room
    player = Player(username, room['outside']);
    
    #welcome player
    print(" \n\n")
    print(f"Your name is {player.name}. You are the premier treasure hunter of your day. \n")

    #room introduction
    print(f"But today, you wake up in a strange place. \n")
    print(f"Your head hurts and you struggle to see straight. \n")
    print(f"You look around, and you see an {player.room.name} \n")
    print("You think you remember how you got there, but are unsure. \n")
    print("Confused. You decide to investigate what happened. \n\n")

    player.room.showItems()

    print("For commands/help, press h\help\n\n")

    while True:
        usr_input = input("Choose a command to continue: ")
        item_command = usr_input.split()
        print("\n")
       
        if usr_input == 'q' or usr_input == 'quit':
            print('You have decided to end your quest. ')
            #stops loop/quits adventure
            break
    
        elif usr_input == 'h' or usr_input == 'help':
            usr_help = """
            HELP:
            ------------------ \n
            DIRECTIONS:\n
            press "n": to travel north
            press "e": to travel east
            press "w": to travel west
            press "s": to travel south\n
            ------------------- \n

            ITEMS:\n
            You can view, add, and remove items in your inventory.

            press "i": to view player's current inventory\n
            press "r": to view current Room's inventory.\n
            
            TO PICK UP ITEMS FOUND IN ROOMS:\n
            Type one of the following "grab", "get", "take" + the name of the item listed in room:\n
            ex: "grab Knife" or "take Treasure"\n
            This will add item to player inventory and remove it from the room's inventory.\n

            TO DROP ITEMS FROM PLAYER INVENTORY:\n
            Type "drop" + the name of the item listed in player's inventory:\n
            ex: "drop Knife"\n
            This will remove item from player inventory and add it to the current room's inventory.\n\n
            -------------------\n
            QUIT: \n
            press "q" or "quit": to quit/exit program
            
            """
            print(usr_help)
        
        elif usr_input == 'i' or usr_input == 'inventory':
            player.showInventory()
        
        elif usr_input == 'r':
            player.room.showItems()

        elif item_command[0] in ['take', 'get', 'grab']:
            for item in player.room.items:
                if item.name.lower() == item_command[1].lower():
                    player.getItem(item)
                    print(f"You picked up {item.name}")
                    player.room.removeItem(item)
                    print(f"{item.name} was removed from Room Items.\n")
        
        elif item_command[0] == 'drop':
            for item in player.inventory:
                if item.name.lower() == item_command[1].lower():
                    player.dropItem(item)
                    print(f"You dropped {item.name}")
                    player.room.addItem(item)
                    print(f"{item.name} was added to Room Items\n")

        elif usr_input == 'n':
            
            try:
                player.room = player.room.n_to
                print(f"You have entered the {player.room.name}  \n")
                print(f"{player.room.description}\n\n" )
                player.room.showItems()
            except:
                if player.room.name == "Grand Overlook":
                    print("Angrily, you kick a rock into the chasm. You hear nothing.")
                    print("It's a long drop. You decide to return back to the south \n\n")

                elif player.room.name == "Treasure Chamber":
                    print("You scream out of frustration. Dust begins to fall, and the walls begin to rumble.")
                    print("Before you cause a cave in, you scurry out the way you came. \n\n")
        
        elif usr_input == 's':
            try:
                player.room = player.room.s_to
                print(f"You have entered the {player.room.name}  \n")
                print(f"{player.room.description}\n\n" )
                player.room.showItems()
            except:
                if player.room.name == "Outside Cave Entrance":
                    print("Oops, you are back where you started. You should return North. \n")
                
                elif player.room.name == "Narrow Passage":
                    print("You're least favorite animal, a snake... is hanging from the vines.")
                    print("Without hesitation, you change course. \n\n")
            
        elif usr_input == 'e':
            try:
                player.room = player.room.e_to
                print(f"You have entered the {player.room.name}  \n")
                print(f"{player.room.description}\n\n" )
                player.room.showItems()
            except:
                if player.room.name == "Outside Cave Entrance":
                    print("There is a thick, dark and ominus forest stares back at you. Was this the way you came?")
                    print("With no light, or other protection, you decide to explore another time...you change course.\n\n")
                
                elif player.room.name == "Grand Overlook":
                    print("The moutain walls sparkle, did you find it?")
                    print("As you get closer, your heart races, you are filled with excitment. Could it be gold?")
                    print("Nope. It's not. Seems like some local animal decided to sneeze all over the wall.")
                    print("Your hands aren't happy with you. ")
                    print("You turn around and go...\n\n")

                elif player.room.name == "Narrow Passage":
                    print("You walk right into the wall. It hurts.")
                    print("You look North, You look West. You decide to go...\n\n ")
                
                elif player.room.name == "Treasure Chamber":
                    print("Something is glittering in the dim light. You investigate.")
                    print("Alas! It's just a piece of tin. But it's not much. Just a very small piece.")
                    print("There is nothing else here, you leave. \n\n")

        elif usr_input == 'w':
            try: 
                player.room = player.room.w_to
                print(f"You have entered the {player.room.name}  \n")
                print(f"{player.room.description}\n\n" )
                player.room.showItems()

            except:
                if player.room.name == "Outside Cave Entrance":
                    print("A gust of wind, nearly blows you over the edge of the cliff.")
                    print("It's a beautiful view, but you dont feel like dying today. You change course.\n\n")

                elif player.room.name == "Grand Overlook":
                    print("There is thick brush. Looks like a mixture of vines and bushes of some sort.")
                    print("You are curious, as you have never seen that type of fauna before.")
                    print("As you get closer, the bushes ruffle.")
                    print("That is all you need see. You turn quickly and run... \n\n")
                  

                elif player.room.name == "Foyer":
                    print("What is that? You slowly move towards vines drapping from the wall.")
                    print("You move the vines, and something jumps out.")
                    print("It's Dr. Forrestal. You found him! But he's been dead a long time.")
                    print("You shake your head, and turn around... North or East. Which way to go?\n\n")
                
                elif player.room.name == "Treasure Chamber":
                    print("The dim light shines on some hyroglypics on the wall. You dust it off.")
                    print("It reads \"Sorry, You're Too Late...Sucka!! (smiley face) \" ")
                    print("Dejected, you pick up a large rock and begin to angrily scrape at the words.")
                    print("There is nothing here. You decide to leave. \n\n")


if __name__ ==  "__main__":
    start_game()