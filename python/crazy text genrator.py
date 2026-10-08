# a program to generate cRazY tExT

# Import Libraries
import random
# genrate a random number between 1 and 0 every time everytime the for loop iterates through each letter in 
upper_or_lower = random.randint(0,1)

def make_text_crazy(text):
    crazy_text = ""
    
    # a loop to randomly decide if a letter be upper or lowercase 
    for char in text:
        # checks if char is a letter
        if char.isalpha():
            if upper_or_lower == 0:                                         # checks if upper_or_lower is 0 it turns that letter Capital 
                new_letter = char.upper()                                
            elif upper_or_lower == 1:                                       # check if upper_or_lower is 1 it turns the letter Lower 
                new_letter = char.lower()    
            crazy_text += new_letter
        else: 
            crazy_text += char
    return crazy_text   

def main():  
    print("Welcome to the CraZy TeXt generator")
    user_text = input("Enter your text: \n ")
    
    crazy_text = make_text_crazy(user_text)
    print(crazy_text) 
main()   