# Hangman game. 

import simplegui
import random

# Media
soundlost = simplegui.load_sound('http://themushroomkingdom.net/sounds/wav/smb/smb_gameover.wav')
soundwin = simplegui.load_sound('http://themushroomkingdom.net/sounds/wav/smb/smb_stage_clear.wav')

# Lists
letters = []
guessed = []
fullyguessed = []

# Global Variables
guessthis = " "
numwords = " "
letter_guess = " "
chances = 6
wordright = " "


def trash_talk():
    # Makes trash talk
     
    num = random.randint(0, 10)
    
    if num == 1:
        print "REKT."
    elif num == 2:
        print "Git g00d"
    elif num == 3:
        print "GG WP"
    elif num == 4:
        print "Being this bad at hangman. LOL."
    elif num == 5:
        print "Mad cause bad"
    elif num == 6:
        print "You have the mental agility of a bagel"
    elif num == 7:
        print "EZ game"
    elif num == 8:
        print "You suck."
    elif num == 9:
        print "2 EZ"
    elif num == 10:
        print "You lost when you pressed play m8"
        
def print_words():
    # Takes in a list of words and prints them on the same line
     
    global guessed
    
    for i in range(len(guessed)):
        print guessed[i],                
    
    
def new_words():
    # Asks the first player how many words they will input, then asks for each word and stores them to a list.  
    
    global letters, fullyguessed, guessthis, numwords
    
    numwords = int(input("Player 1: Enter the number of words you would like Player 2 to guess"))
    
    for s in range(numwords):
        guessthis = str(input("Player 1: Enter a words you would like Player 2 to guess"))
        letters.extend(list(guessthis))
        letters.append(" ")
        

def hide_words():
    # Takes in a list of words and makes a list of hangman chacters with all of the letters replaced by underscores
   
    global guessed, fullyguessed, guessthis, numwords
    
    for s in range(numwords):
        
        for i in range(len(guessthis)):
            guessed.append("_")
            fullyguessed.append("_")
        
        guessed.append(" ")
        fullyguessed.append(" ") 


def reveal_letter():     
    #Takes in a letter, checks whether the letter is in the word list and replaces the underscore in the hangman list by letter.
    
    global letters, guessed, chances, letter_guess, wordright
    
    letter_guess = str(input("Player 2: Guess a letter."))
    
    if letter_guess in letters:
        
        wordright = 1
        
        # Allows porgram to repeatdly search for same letters if multiple of the same letters exist in a phrase. 
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
        
        wordright = 0
        chances -= 1
        
        if chances > 0:
            print "\n\n", letter_guess, "is not in list! You have", chances, "chances left"
            
def play_game(): 
    # Main game function. Gets new words from player 1, hides the word, and asks for a guess and reveals the letter guessed. Keeps
    # keeps track of number of chances remaining and whether the game has been won or lost.
    
    global chances, guessed, letters, fullyguessed, letter_guess, soundlost, soundwin, soundwrongword
    
    new_words()
    hide_words()
    print_words()

    while chances > 0:
        
        reveal_letter()
        
        if wordright == 0:
            trash_talk()
        
        if letters == fullyguessed:
            print "\nPlayer 2 Wins!"
            soundwin.play()
            break
            
            
    else: 
        print "\n\n", letter_guess, "is not in list! Player 2 loses"
        soundlost.play()
        
        
play_game()
