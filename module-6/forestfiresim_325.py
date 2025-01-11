"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

###all additions marked by "##6.2"

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '

##6.2: add marker for water
WATER = 'W'

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.02  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5

def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        bext.clear()
        displayForest(forest)
        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees (##6.2: as long as they're not water):
                            if (forest.get((x + ix, y + iy)) == TREE) and forest.get((x + ix, y + iy)) != WATER:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                    
                ##6.2: if the spot is water, it stays water
                elif forest[(x,y)] == WATER:
                    # Pools of water are unaffected
                    nextForest[(x,y)] = WATER
                    
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    
    ##6.2: establish values to set for water...because using multiple ranges causes KeyError
    water_xvalue = [36,37,38,39,40,41,42]
    water_yvalue = [10,11,12,13,14,15,16,17,18,19]
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            
            ##6.2: if x and y values match water values, this spot is water
            if x in water_xvalue and y in water_yvalue:
                forest[(x, y)] = WATER
                
            else:
                if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                    forest[(x, y)] = TREE  # Start as a tree.
                else:
                    forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
                
            ##6.2: display water on screen
            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')
                
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.