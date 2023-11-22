import random
import words 
import string


def get_valid_word(word):
    word = random.choice(words)
    while '_' in word or '' in word:
        word = random.choice(words)
        return word
    

def hangman():
    word = get_valid_word(words) 

    word_letters = set(word) # letters in the word
    alphabet = set(string.ascil_uppercase)
    used_letters = set() # what the user has guessed

    lives = 7

  # getting user input 
while len(word_letters)>0:
   #letter used
   #''.join(['a','b','cd']) -->'a b cd'
   print('You have ',lives,'lives left and you have used those letters:',''.join(used_letters))

#What current word is (eg W-R D)
wors_list = [letter if used_letters else '_' for lettetr in word]
print('current word:',''.join(word_list ))

user_input = input('Guess a letter:').upper()
if user_input in alphabet - used_letters:
   user_input.__add__(user_letter)
   if user_input in word_letter:
       word_letters.remove(user_letter)

elif user_input in used_letters:
 print ('You have already used that character.Please try again. ')   

else: 
 print('Invalid character. Please try again.')

# gets here when  len(word_letters) == 0 or when lives == 0 
 if lives ==0:
    print('You died, sorry.The word was',word)
 else:
  print('You guessed the words', word,'!!')

 hangman()
print(user_input)       
    
    