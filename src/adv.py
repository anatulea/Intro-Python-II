from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",  "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

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

name = input('What is your name? ')
def start_game(name):
    print(f'Welcome to the game {name}!')
start_game(name)
    
player_one = Player(name, room['outside'])

playing = True
while playing:
    print(f'\nRoom: {player_one.current_room.name}')
    print(f'Description : {player_one.current_room.description}\n')
    selection = input('Where do you go next? Use "n", "s", "e", "w", or "q"(quit) to navigate the rooms: ')
    
    if selection[0].lower() == 'e':
        try:
            player_one.current_room = player_one.current_room.e_to
        except:
            print('\nThere is no room to the East')
    elif selection[0].lower() == 'n':
        try:
            player_one.current_room = player_one.current_room.n_to
        except:
            print('\nThere is no room to the North')
    elif selection[0].lower() == 'w':  
        try:
            player_one.current_room = player_one.current_room.w_to
        except:
            print('\nThere is no room to the West')
    elif selection[0].lower() == 's':
        try:
            player_one.current_room = player_one.current_room.s_to
        except:
            print('\nThere is no room to the South')
    elif selection[0].lower() == 'q':
        playing = False
        print('\nThank you for playing!')
        break
    else:
        print('\nPlease enter a valid command!') 