import random
NUM_digits = 3
Max_guesses = 10

def main():
  print('''Bagels, a deductive logic game.
  By Al Sweigart al@inventwithpython.com  I am thinking of a {}-digit number with no repeated digits.
  Try to guess what it is. Here are some clues:
  When I say:    That means:
   Pico         One digit is correct but in the wrong position.
   Fermi        One digit is correct and in the right position.
   Bagels       No digit is correct.''')
 
  while True:
        secretNumber = getSecretNum()
        print('I have though up a number')
        print('You have {} guesses to get it.'.format(Max_guesses))
        
        numGuesses = 1
        while numGuesses <=Max_guesses:
            guess = ''
            while len(guess)!= NUM_digits or not guess.isdecimal():
                print('guess #{}: '.format(numGuesses))
                guess = input('> ')
                
            clues = getClues(guess, secretNumber)
            print(clues)
            numGuesses +=1
            
            if guess == secretNumber:
                break
            if numGuesses >Max_guesses:
                print('You ran out of guesses.')
                print('The answer was {}.',format(secretNumber))
                
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing')
        
        
def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretNum  = ''
    for i in range(NUM_digits):
        secretNum += str(numbers[i])
    return secretNum
    
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    clues  = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
