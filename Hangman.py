# Hangman game. 
chances = 5
letters = []
guessed = []
fullyguessed = []
guessthis = " "
numwords = " "


def print_words():
    # Takes in a list of words and prints them on the same line
     
    global guessed
    
    for i in range(len(guessed)):
        print guessed[i],                
    
    
def new_words():
    # Asks the first player how many words they will input, then asks for each word and stores them to a list.  
    
    global letters
    global guessed
    global fullyguessed
    global guessthis
    global numwords
    
    numwords = int(input("Player 1: Enter the number of words you would like Player 2 to guess"))
    
    for s in range(numwords):
        guessthis = str(input("Player 1: Enter a words you would like Player 2 to guess"))
        letters.extend(list(guessthis))
        letters.append(" ")


def hide_words():
    # Takes in a list of words and makes a list of hangman chacters with all of the letters replaced by underscores
   
    global guessed
    global fullyguessed
    global guessthis
    global numwords
    
    for s in range(numwords):
        
        for i in range(len(guessthis)):
            guessed.append("_")
            fullyguessed.append("_")
        
        guessed.append(" ")
        fullyguessed.append(" ") 


def reveal_letter():     
   #Takes in a letter, checks whether the letter is in the word list and replaces the underscore in the hangman list by letter.
    
    global letters
    global guessed
    
    letter_guess = str(input("Player 2: Guess a letter."))
    
    if letter_guess in letters:
            
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
        chances -= 1
        
    
    
def play_game(): 
# Main game function. Gets new words from player 1, hides the word, and asks for a guess and reveals the letter guessed. Keeps
# keeps track of number of chances remaining and whether the game has been won or lost.
    
    global chances
    global guessed
    global letters
    global fullyguessed
    
    new_words()
    hide_words()
    print_words()


    while chances > 0:
        
        reveal_letter()
    
        print "\n"
        
        if letters == fullyguessed:
            print "\nPlayer 2 Wins!"
            break
            
    else: 
        print "\nPlayer 2 loses"
        


play_game()
