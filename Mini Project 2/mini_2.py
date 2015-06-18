# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

secret_number = 0
in_guess = 0
n = 0
# helper function to start and restart the game
def new_game(x):
    print "___________________________________\n"
    print "Started a new game with range 0 to",x
    global n
    n = math.ceil(math.log((x-0+1),2))
    print "Total Number of guesses allowed are",n
    # initialize global variables used in your code here
    if x == 100:
        range100()
    elif x == 1000:
        range1000()    	
    
def newgame_range100():
    x = 100
    new_game(100)

def newgame_range1000():
    x = 1000
    new_game(1000)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number 
    secret_number = random.randrange(0, 100)
    #print "Secret Number is ", secret_number

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number 
    secret_number = random.randrange(0, 1000)
    #print  "Secret Number is ", secret_number
    
def input_guess(guess):
    # main game logic goes here
    global in_guess
    in_guess = int(guess)
    global n
    n  = n-1
    print "\nGuess was", in_guess
    print "Remaning number of gusses are", n
    if n < 0:
        print "Game Over You Loose \n"
        new_game(100)
        
    else:
        if in_guess < secret_number:
            print "Higher"
        elif in_guess == secret_number:
            print "Correct"
            print "You Win !! \n"
            new_game(100)
            
        else:
            print "Lower"
    

    
# create frame
frame = simplegui.create_frame("Test Frame", 200, 200)
input = frame.add_input("Guess a Number", input_guess, 100)
frame.add_button("New game in range 100",newgame_range100, 200 )
frame.add_button("New game in range 1000",newgame_range1000, 200 )
# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game(100)


# always remember to check your completed program against the grading rubric