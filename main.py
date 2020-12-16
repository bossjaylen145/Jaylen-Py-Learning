import random
import logging
from PIL import Image
from dice_config import *

global randomized, again
global global_variable


def create_global_variable():
    global global_variable  # must declare it to be a global first
    # modifications are thus reflected on the module's global scope
    global_variable = 'randomized'


# logging input for debug
logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
restart = 0
# asking for input
roll = str(input('Would you like to roll the dice?'))

# checking for numbers in string
contains_digit = False
for character in roll:
    if character.isdigit():
        contains_digit = True
logging.info('"' + roll + '"' + ' has digit ' + str(contains_digit))

# checking for whitespaces
whitespace = ' '
contains_whitespace = False
for whitespace in roll:
    if whitespace.isspace():
        contains_whitespace = True
        print('the word ' + '"' + roll + '"' + ' is invalid')
logging.info('"' + roll + '"' ' has whitespace ' + str(contains_whitespace))

# check if cancel words if so program exists
if roll in cancel:
    logging.info('Canceled dice rolling')
    print('Cancelling')
    exit(exit())

# checking for alternative words
if roll in alternative_words:
    r = 1
if restart == 1:
    r = 1
    logging.info('"' + roll + '"' + ' is a valid word')

# generating random int between 1 and 6
randomized = random.randint(1, 6)


def randomized1():
    # opening the images
    if str(randomized) == 1:
        print('You rolled ' + str(randomized))
        logging.info('Successfully rolled ' + str(randomized))
        im = Image.open("Assets\\img\\dice1.png")
        im.show()
        logging.info('Successfully opened dice1.png')
    if randomized == 2:
        print('You rolled ' + str(randomized))
        logging.info('Successfully rolled ' + str(randomized))
        im = Image.open("Assets\\img\\dice2.png")
        im.show()
        logging.info('Successfully opened dice2.png')
    if randomized == 3:
        print('You rolled ' + str(randomized))
        logging.info('Successfully rolled ' + str(randomized))
        im = Image.open("Assets\\img\\dice3.png")
        im.show()
        logging.info('Successfully opened dice3.png')
    if randomized == 4:
        print('You rolled ' + str(randomized))
        logging.info('Successfully rolled ' + str(randomized))
        im = Image.open("Assets\\img\\dice4.png")
        im.show()
        logging.info('Successfully opened dice4.png')
    if randomized == 5:
        print('You rolled ' + str(randomized))
        logging.info('Successfully rolled ' + str(randomized))
        im = Image.open("Assets\\img\\dice5.png")
        im.show()
        logging.info('Successfully opened dice5.png')
    if randomized == 6:
        print('You rolled ' + str(randomized))
        logging.info('Successfully rolled ' + str(randomized))
        im = Image.open("Assets\\img\\dice6.png")
        im.show()
        logging.info('Successfully opened dice6.png')


randomized1()

# asking if you want to roll the dice again
again = str(input('Would you like to role the dice again?'))
if again in cancel:
    logging.info('Canceled dice rolling')
    print('Cancelling')
    exit(exit())
if again in alternative_words:
    restart = 1
    # generating random int between 1 and 6
    randomized = random.randint(1, 6)
    randomized1()
