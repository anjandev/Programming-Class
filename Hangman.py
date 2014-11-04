# Hangman game By Anjan Momi

import simplegui
import random

# Media
sound_lost = simplegui.load_sound('http://themushroomkingdom.net/sounds/wav/smb/smb_gameover.wav')
sound_win = simplegui.load_sound('http://themushroomkingdom.net/sounds/wav/smb/smb_stage_clear.wav')

# Lists
letters = []
guessed = []
fully_guessed = []
guessed_letters = []

# Global Variables
guess_this = " "
num_words = " "
letter_guess = " "
chances = 6
word_right = " "


def already_guessed():
    # Takes in a letter, Checks whether player 2 has already guessed that word and if he has it does not take away a chance but rather asks for another word.
    
    global guessed_letters, letter_guess
    
    letter_guess = str.lower(input("Player 2: Guess a letter."))
    
    if letter_guess in guessed_letters:
        print "_____________________________________________________________"
        print "\nYou have already guessed", letter_guess, ". Please enter a different letter"
        already_guessed()
        
    else:
        print "_____________________________________________________________"
        print "\nYou guessed", letter_guess,", is it in the phrase?",
        guessed_letters.append(letter_guess)
    
    
def draw_hang():
    # Draws a hangman based on how many chances the player 2 has.
    
    global chances
    
    if chances == 6:
        print "\n",
        print """                     ______
                    |	   
                    |      
                    |      
                    |
                  __|_________
                 |            |"""
        
    elif chances == 5:
        print "\n",
        print """                     ______
                    |	   |
                    |      O
                    |      
                    |
                  __|_________
                 |            |"""
        
    elif chances == 4:
        print "\n",
        print """                     ______
                    |	   |
                    |      O
                    |      |
                    |
                  __|_________
                 |            |"""
        
    elif chances == 3:
        print "\n",
        print """                     ______
                    |	   |
                    |      O
                    |     \|
                    |
                  __|_________
                 |            |"""
                
    elif chances == 2:
        print "\n",
        print """                     ______
                    |	   |
                    |      O
                    |     \|/
                    |     
                  __|_________
                 |            |"""

                
    elif chances == 1:
        print "\n",
        print """                     ______
                    |	   |
                    |      O
                    |     \|/
                    |      |
                    |     /
                  __|_________
                 |            |"""
        
    else:
        print """                     ______
                    |	   |
                    |      O
                    |     \|/
                    |      |
                    |	  / \                                  
                  __|_________                          
                 |            |"""
        

def trash_talk():
    # Makes trash talk if the player 2 gets a word wrong
     
    num = random.randint(0, 10)
    
    if num == 1:
        print "REKT.\n",
        
    elif num == 2:
        print "Git g00d\n",
        
    elif num == 3:
        print "GG WP\n",
        
    elif num == 4:
        print "Being this bad at hangman. LOL.\n",
        
    elif num == 5:
        print "Mad cause bad\n",
        
    elif num == 6:
        print "You have the mental agility of a bagel\n",
        
    elif num == 7:
        print "EZ game\n",
        
    elif num == 8:
        print "You suck.\n",
        
    elif num == 9:
        print "2 EZ\n",
        
    elif num == 10:
        print "You lost when you pressed play m8\n",
        
        
def print_words():
    # Takes in a list of words and prints them on the same line
     
    global guessed
    
    for i in range(len(guessed)):
        print guessed[i],                
    
    
def new_words():
    # Asks the first player how many words they will input, then asks for each word and stores them to a list.  
    
    global letters, guess_this, num_words
    
    num_words = int(input("Player 1: Enter the number of words you would like Player 2 to guess"))
    
    for s in range(num_words):
        guess_this = str.lower(input("Player 1: Enter a words you would like Player 2 to guess"))
        letters.extend(list(guess_this))
        letters.append(" ")
        

def hide_words():
    # Takes in a list of words and makes a list of hangman chacters with all of the letters replaced by underscores
   
    global guessed, fully_guessed, guess_this, num_words
    
    for s in range(num_words):
        
        for i in range(len(guess_this)):
            guessed.append("_")
            fully_guessed.append("_")
        
        guessed.append(" ")
        fully_guessed.append(" ") 


def reveal_letter():     
    #Checks whether the letter is in the word list and replaces the underscore in the hangman list by letter.
    
    global letters, guessed, chances, letter_guess, word_right
         
    if letter_guess in letters:
        # Tells the if statement after reveal_letter() in play_game() not to do any trashtalking
        word_right = 1
        
        print "\nThe letter", letter_guess, "is in the phrase!",
        
        # Allows porgram to repeatdly search for multiple instances of the same letter if multiple instances of the same letters exist in the phrase. 
        for i in range(letters.count(letter_guess)):
            # Finds the place of the letter player 2 guessed in letters list 
            guessednum = letters.index(letter_guess)
            # Deletes the _ placeholder from guessed list and inserts the proper letter.
            guessed.pop(guessednum)
            guessed.insert(guessednum, letter_guess)
            # Deletes the guessed letter from the letters list and inserts a place holder.
            letters.pop(guessednum)
            letters.insert(guessednum, "_")
            
        print "\n"
        
        for i in range(len(guessed)):
            print guessed[i],
             
    else:
        # Tells the if statement after reveal_letter() in play_game() to do trashtalking.
        word_right = 0
        
        chances -= 1
        
        if chances > 0:
            print "\n", letter_guess, "is not in the phrase! You have", chances, "chance(s) left."
           
            
def play_game(): 
    # Main game function. Gets new words from player 1, hides the word, and asks for a guess and reveals the letter guessed. Keeps
    # keeps track of number of chances remaining and whether the game has been won or lost.
    
    global chances, guessed, letters, fully_guessed, letter_guess, sound_lost, sound_win
    
    new_words()
    hide_words()
    print_words()

    while chances > 0:
               
        draw_hang()
        already_guessed() 
        reveal_letter()
        
        if word_right == 0 and chances > 0:
            trash_talk()
        
        if letters == fully_guessed:
            print "\nPlayer 2 Wins!"
            sound_win.play()
            break
            
    else: 
        print "\n", letter_guess, "is not in the phrase! Player 2 loses."
        trash_talk()
        sound_lost.play()
        draw_hang()
        
        
play_game()
