import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']    
words= {'Colors':'''red orange yellow green blue indigo violet white black 
        brown gray fiusha magenta pink cyan'''.split(),
  'Shapes':'''square triangle rectangle circle ellipse rhombus trapezoid
      pentagon hexagon septagon octagon nonagon decagon'''.split(),
  'Fruits':'''apple orange lemon lime pear watermelon grape grapefruit cherry
    banana cantaloupe mango strawberry tomato avocado blueberry raspberry blackberry apricot
    pineapple'''.split(),
  'Animals':'''ant baboon badger bat bear beaver camel cat clam cobra cougar
  coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
  lion lizard llama mole monkey moose mouse mule newt otter owl panda 
  parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
  skunk sloth snake spider stork swan tiger toad trout turkey turtle 
  weasel whale wolf wombat zebra koala kangaroo'''.split(),
  'Countries':'''mexico unitedstatesofamerica alaska canada greenland germany italy france
  spain bolivia brazil argentina chile honduras belize guatemala cuba bahamas jamaica 
  dominicanrepublic czechrepublic haiti elsalvador nicaragua panama costarica puertorico 
  colombia venezuela guyana surinam guyanafrancesa peru ecuador uruguay paraguay portugal 
  sweden norway northkorea southkorea china japan mongolia bangladesh siria botswana uganda 
  angola mauritania niger nigeria chad libya egypt algeria morocco mali sudan ethiopia eritrea 
  djibouti somalia senegal guineabissau guinea sierraleone liberia ivorycoast burkinafaso ghana 
  togo benin cameroon centralafricanrepublic equatorialguinea kenya gabon republicofcongo 
  democraticrepublicofcongo rwanda burundi tanzania zambia malawi mozambique namibia zimbabwe
  southafrica lesotho madagascar switzerland austria bosniaandherzegovina croatia bulgaria hungary 
  romania slovakia slovenia netherlands finland iceland unitedkingdom ireland belgium luxembourg poland belarus estonia 
  latvia ukraine lithuania montenegro sanmarino albania macedonia greece moldova nicosia denmark 
  turkey iraq iran israel saudiarabia qatar unitedarabemirates yemen oman kuwait armenia georgia 
  jordan lebanon azerbaijan pakistan afghanistan turkmenistan uzbekistan tajikistan kyrgyztan kazakhstan 
  india nepal cashmere myanmar laos vietnam thailand cambodia philippines ukraine russia malaysia 
  indonesia papuanewguinea australia tasmania newzealand'''.split()} 
  
def getRandomWord(wordDict):
    #This function returns a random string from the passed dictionary of the lists of strings and its key
    #First, randomly select a key from the dictionary:    
    wordKey= random.choice(list(wordDict.keys()))
    #Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey])-1)
    
    return [wordDict [wordKey] [wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    
    blanks= '_' * len(secretWord)
    
    for i in range(len(secretWord)): #Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            
    for letter in blanks: #Show the secret word with spaces between each letter.
        print(letter, end=' ')
    print()
    
def getGuess(alreadyGuessed):
    '''Returns the letter the player entered. This function makes sure the player entered
    a single letter and not something else.'''
    
    while True:
        print ('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
             print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
             print('Please enter a LETTER.')
        else:
            return guess
 
def playAgain(): 
    #This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

 
print('H A N G M A N')

difficulty='X'
while difficulty not in ['E', 'M', 'H']:
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty= input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
    
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False
 
while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)
 
    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)
 
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break  
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord +
                   '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

         #Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet= getRandomWord(words)
        else:
            break
    