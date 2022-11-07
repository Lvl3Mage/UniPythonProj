import random
target = []
while len(target) < 4:
    rand = random.randint(0,9)
    if(not rand in target):
        target.append(rand)
guess = []
print(target)
while guess != target:
    guess = []
    guessStr = ''
    while len(guessStr) != 4:
        guessStr = input("Enter your guess (4 numbers): ")
    for digit in guessStr:
        guess.append(int(digit))
    if(guess != target):
        correctGuesses = 0
        misplacedGuesses = 0
        for i in range(len(guess)):
            if(target[i] == guess[i]):
                correctGuesses +=1
            elif(guess[i] in target):
                 misplacedGuesses += 1
        print("Correct guesses: {0} | Misplaced guesses {1}".format(correctGuesses, misplacedGuesses))
        
print("You guessed correctly!")   

    