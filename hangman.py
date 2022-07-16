from wordlist import word_list;
import random;
import argparse

secret_Word = ""
letters_Guessed = ""
# Then number of turns before player loses
failureCount = 3

# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-w", "--Word", help = "What word to guess?", default = "")
parser.add_argument("-g", "--Guesses", help = "How many guesses is allowed?", default = 6)

 # Read arguments from command line
args = parser.parse_args()
 
if args.Word:
    print("Word set to: % s" % args.Word)
    secret_Word = args.Word
if args.Guesses:
    try:
        AllowedGuesses = int(args.Guesses)
        print("Guesses set to: % s" % AllowedGuesses)
        failureCount = AllowedGuesses
    except ValueError as verr:
        print("Invalid number of guesses: %s" % verr)
        pass # do job to handle: s does not contain anything convertible to int
    except Exception as ex:
        print("Unknown error: %s" % ex)
        pass # do job to handle: Exception occurred while converting to int

# pick a random word from the word list if secret word is not set
if (not (secret_Word and not secret_Word.isspace())):
    secret_Word = random.choice(word_list)

#loop until the player has made too many failed attempts
#will 'break' loop if they succed instead
while failureCount > 0:
    
    #get the guessed letter from the player
    guess = input("Enter a letter: ")

    if guess in secret_Word:
        #player guessed a correct letter!
        print(f"Correct! There is one or more {guess} in the secret word.")
    else:
        failureCount -= 1
        print(f"Incorrect. There are no {guess} in the secret word. {failureCount} turn(s) left.")

    #maintain a list of all letters guessed
    letters_Guessed = letters_Guessed + guess
    wrongLetterCount = 0

    for letter in secret_Word:
        if letter in letters_Guessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount +=1
    print("")
    #if there were no wrong letters, then the player won!
    if wrongLetterCount == 0:
        print(f"Congratulations! The secret word was: {secret_Word}. you won!")
        break
else:
    print(f"Sorry, you didn't win it this time. The word was: {secret_Word} Try Again!")
