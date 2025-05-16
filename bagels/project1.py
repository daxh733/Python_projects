import random

NUM_DIGIT=3
MAX_GUESS=10

def main():
    print("Welcome to the world of guesses")

    while True:
        secret_num=getSecretNum()
        print('I have thought up a number.')
        print(f'you have {MAX_GUESS} to get it.')
        numGuess=1
        while numGuess<=MAX_GUESS:
            guess=''
            while len(guess)!=NUM_DIGIT or not guess.isdecimal():
                print(f'guess {numGuess}')
                guess=input('>')

            clues=getClues(guess,secret_num)
            print(clues)
            numGuess+=1

            if guess==secret_num:
                break
            if numGuess>MAX_GUESS:
                print('You are ran out of guesses')
        print('Do you want to know the answer?(yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        if not input('> ').lower().startswith('n'):
            print(secret_num)
        
    print('Thanks for playing!')

def getSecretNum():
    numbers=list('0123456789')
    random.shuffle(numbers)
    secretNum=''
    for i in range(NUM_DIGIT):
        secretNum+=str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess ==secretNum:
        return 'You got it'
    
    clues=[]
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
        
    if len(clues)==0:
        return 'Bagels'
    
    else:
        clues.sort()
        return ' '.join(clues)
    

if __name__=='__main__':
    main()












