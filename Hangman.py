# Hangman game

def play_game():
    
    chances = 5
    
    guessthis = str(input("Player 1: Enter a word you would like Player 2 to guess"))
    
    letters = list(guessthis)
    numlet = len(letters)
    
    guessed = []
    fullyguessed = []
    
    for i in range(numlet):
        guessed.append("_")
        fullyguessed.append("_")
    
    print guessed

    while chances > 0:

        letter_guess = str(input("Player 2: Guess a letter."))
        
        if letter_guess in letters:
			# Finds the place of the letter player 2 guessed in letters list 
            guessednum = letters.index(letter_guess)
            # Deletes the _ placeholder from guessed list and inserts the proper letter.
            guessed.pop(guessednum)
            guessed.insert(guessednum, letter_guess)
            # Deletes the guessed letter from the letters list and inserts a place holder.
            letters.pop(guessednum)
            letters.insert(guessednum, "_")
            print "\n", guessed
            
            if letters == fullyguessed:
                print "Player 2 Wins!"
                break
            
        else:
            chances -= 1
    
    else: 
        print "player 2 loses"
        
        
play_game()
