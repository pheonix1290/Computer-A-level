import random

HANGMAN_PICS = ['''
  -----
  |   |
      |
      |
      |
      |
=========''', '''
  -----
  |   |
  O   |
      |
      |
      |
=========''', '''
  -----
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  -----
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  -----
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  -----
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["sloth" , "koala" , "leopard" , "tiger" , "panda" , "elepahant","giraffe"]

def choose_random_word(words):
    word = random.choice(words)
    return word

def main():
    print("Welcome to Hnagman!")
    secret_word = choose_random_word(words)
    blanks = list( "_" * len(secret_word)  )
    
    print(HANGMAN_PICS[0])
    print(" ".join(blanks))
    
    incorrect_letters = 0
    while "_" in blanks and incorrect_letters < 6:
        letter = input("Guess a letter:")
        
    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                blanks[i] = letter    
            else:
                incorrect_letters += 1
            print(HANGMAN_PICS[incorrect_letters])        
            print(" ".join(blanks))
    if incorrect_letters == 6:
        print("You lose! The word was", secret_word)
    else:
        print("well done!")
        
main            