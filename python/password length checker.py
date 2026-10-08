def check_password_score(password):

    score = 0
    has_numbers = False  #boolean
    has_uppercase = False
    has_lowercase = False
    has_special_characters = False


    if len(password) > 8 :
        score += 1


    for character in password:
        if character.isalpha():
            #checks if the character is upper , if true has_uppercase become true and stops beign false User gains 1 point
            if character.isupper():
                score += 1
                has_uppercase = True


            if character.islower():
                #checks if the character is lower , if true has_lowercase become true and stops beign false User gains 1 point
                if not has_lowercase:
                    score += 1
                    has_lowercase = True


        if character.isdigit():
            #checks if the character has a number , if true has_number become true and stops beign false User gains 1 point
            if not has_numbers:
                score += 1
                has_numbers = True

        if not character.isalnum():
            #checks if the character is not either a letter or number , if true has_special_character become true and stops beign false User gains 1 point
            if not has_special_characters:
                score += 1
                has_special_characters = True
    return score
def check_password_strength(score):
    if score == 5:
        print("Strong password!")
    elif score >= 3:
        print("Moderate password.")
    else:
        print("Weak password!")

def main():
    print("Welcome to the Password Strength Checker!")
    print("for security reasons, we recommend that you don't enter your real passwords here.")

    password = input("Enter your password: \n ")

    password_score =  check_password_score(password)
    check_password_strength(password_score)