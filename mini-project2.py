# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    
    # remove this when you add your code    
    global secret_number, count, num_range
    secret_number = random.randrange(0, 100)
    count = 7
    num_range = 100
    print "New game, Range is from 0 to 100"
    print "Number of remaining guesses is " + str(count)
    print ""
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    global secret_number, count, num_range     
    secret_number = random.randrange(0, 100)
    count = 7
    num_range = 100
    print "New game, Range is from 0 to 100"
    print "Number of remaining guesses is " + str(count)
    print ""
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global secret_number, count, flag, num_range
    flag = False
    secret_number = random.randrange(0, 1000)
    count = 10
    num_range = 1000
    print "New game, Range is from 0 to 1000"
    print "Number of remaining guesses is " + str(count)
    print ""
def input_guess(guess):
    print "Guess was " + guess
    # main game logic goes here	
    global count
    if int(guess) > secret_number:
        count -= 1        
        print "Number of remaining guesses is", count
        print "Lower"        
    elif int(guess) < secret_number:
        count -= 1                
        print "Number of remaining guesses is", count
        print "Higher"            
    else:
        print "Correct"
        print ""
        if num_range == 100:
            range100()
        else:
            range1000()
    if count == 0:
        print ""
        print "You ran out of guesses.  The number was " + str(secret_number)
        print ""
        if num_range == 100:
            range100()
        else:
            range1000()
    # remove this when you add your code
    print ""

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("range[0, 100)", range100)
frame.add_button("range[0, 1000)", range1000)
frame.add_input("input_guess", input_guess, 100)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
