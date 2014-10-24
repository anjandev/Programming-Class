# Hangman game

def play_game():
    
    chances = 5
    letters = []
    guessed = []
    fullyguessed = []
    
    numwords = int(input("Player 1: Enter the number of words you would like Player 2 to guess"))
    
    for s in range(numwords):
        guessthis = str(input("Player 1: Enter a words you would like Player 2 to guess"))
        letters.extend(list(guessthis))
        letters.append(" ")
        for i in range(len(guessthis)):
            guessed.append("_")
            fullyguessed.append("_")
        guessed.append(" ")
        fullyguessed.append(" ")
        
    
    for i in range(len(guessed)):
        print guessed[i], 

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
            
            print "\n"
            
            for i in range(len(guessed)):
                print str(guessed[i]),
            
            if letters == fullyguessed:
                print "\nPlayer 2 Wins!"
                break
            
        else:
            chances -= 1
    
    else: 
        print "\nPlayer 2 loses"
        
        
play_game()