# Cat DayCare Simulation

#-----------------------------------------
import random
#-----------------------------------------

#-----------------------------------------
# Classes
#-----------------------------------------

class Cat:
    def __init__(self, name, breed, owner, age):
        self.name = name     # Stores the name of the cat 
        self.breed = breed   #Stores the breed of the cat
        self.owner = owner   # Stores the name of the cat's owner
        self.age = age       # Stores the age of the cat
        
#-----------------------------------------
#Methods
#----------------------------------------
# These our the actions that the cat can perform        
    
    # This method allow the cat to purr 
    def purr(self):
        return f"{self.name} is purring." 
    
    # This method allow the cat to perfom the action of sleepping 
    def sleep(self):
        return f"{self.name} is sleeping"
    
    # This method allow the cat to tell the user their identity or backgrounf
    def identify(self):
        return f"Meow ! My name is {self.name} , I am a { self.breed} and my owner is {self.owner}. I am {self.age} years old."
    
#-------------------------------------------
#List of Cat objects
#------------------------------------------
    # List of All the cats in daycare and their profile
cat_profile = [
    Cat ("Luma" , "Siamese" , "Maya" , 30) ,
    Cat ("Oliver" , "Maine Coon" , "Liam" , 7) ,
    Cat ("Mittens" , "Persian" , "Emma" , 5),
    Cat ("Mochi" , "Scottish Fold" , "Chloe" , 2),
    Cat ("Simba" ,"Bengal" , "Noah" , 5)
] 

#------------------------------------------------
#   

#-------------------------------------------------
# Main Program
#-------------------------------------------------
print("Welcome to Cat DayCare!")  

user_name = input("What is your name ?")
print(f"Hi {user_name} how could we help you today . Below is our options:\n 1. Drop off a cat in Day care \n 2. Find out about a random cat")

drop_cat_off = input ("Drop off a cat in Day care : yes/no/y/n")

if drop_cat_off.lower() in ["yes", "y"]:
    cat_name = input(f"What is the name of your cat {user_name}? ")
    cat_breed = input ("What is tje breed of teh cat ?")
    cat_owner = user_name
    cat_age = int(input("What is the age of the cat ? "))
    
    new_cat_profile = Cat (cat_name, cat_breed, cat_owner, cat_age)
    cat_profile.append(new_cat_profile) # adds the new cat profile to teh bottom of the list of our cat proiles       
elif drop_cat_off.lower() in ["no", "n"] :
    random_cat_profile = input("Do want to find out about a random cat yes/no/y/n")
    if random_cat_profile.lower() in ["yes", "y"]:
        random_cat = random.choice(cat_profile) # choose a random cat proile form the list
        
        print("What do you want to know about the cat you have choosen?")
        option = input ("Choosen from the option belowe: \n 1. Name \n 2. Breed \n 3. Age \n 4. All ")
        
        if option.lower() == "name":
            print(f"The name of the lucky cat is {random_cat.name}.")
        elif option.lower() == "breed":
            print(f"The lucky cat's breed is {random_cat.breed}")
        elif option.lower() == "age":
            print(f"The lucky cat's age is {random_cat.age} years old")
        elif option.lower() == "all":
            print(random_cat.identify()) 
            print(
                 r"""
                /\_/\  
               ( o.o ) 
               / > m )   my is the cat's paw and it's been licked
               |  _/ |  
               |_| |_|  
            """
            )       
        else:
            print("Sorry today musn't be your day,try again tomorrow who knows you might find your lucky cat  < | | >")
    elif random_cat_profile.lower() in ["no", "n"]:
        print(
            r"""
           /\_/\  
          ( o.o ) 
           > ^ <  
        """
        )            
        print("Awwn to bad, sorry we can't help you today,well have a nice day.")    
        
    random_action = input ("Do want to know what  your random cat is doing option: yes/no")
    
    if random_action.lower() in ["yes", "y"]:
        random_action =  random.choice([random_cat.purr(), random_cat.sleep()])
        print(f"Your random lucky cat  {random_action}")
    else:
        print("Awwn to bad, sorry we can't help you today,well have a nice day.")          