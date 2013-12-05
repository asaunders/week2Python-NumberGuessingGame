import random

guessesMade = 0

print('Welcome to Adam's random number guessing game! Please enter your name now.')
PlayerName = input(0)

theNumber = random.randint (1, 100)
print('Glad you can join us, ' + PlayerName '. There's a number between 1 and 100 that I'm thinking of. I'll give you 10 chances to guess it. Good luck!')

while guessesMade < 10:
      print('Guess the number!')
      PlayerGuess = input()
      PlayerGuess = int(guess)

      guessesMade = guessesMade + 1

      if PlayerGuess < theNumber:
          print('Too low!')

      if PlayerGuess > theNumber:
          print('Too high!')

      if PlayerGuess == theNumber;
          break

if PlayerGuess == theNumber:
      guessesMade = str(guessesMade)
      print('Congratulations, ' + PlayerName + '! It took ' + guessMade + ' guesses for you to find my number.')

if PlayerGuess != theNumber:
      number = str(number)
      print('I'm sorry. The correct answer was ' + theNumber)
            
