# Cat DayCare Simulation

#-----------------------------------------
import random
#-----------------------------------------
# Traits List
#-----------------------------------------
core_traits = ["lazy" , "greedy" , "shy" ,
               "affectionate" ,  "curious" , "grumpy",
               "playful", "adventourous" , "generous" , 
                "wise" , "spoilt" , "energetic"]

trait_modifier = { "greedy" : {"hunger" : 2, "energy" : 0, "fulfillment" : 0, "soical" :0 },
                   "lazy" : {"hunger" : 0, "energy" : -1, "fulfillment" : 0, "social" : 0},
                   "energetic" : {"hunger" : 0 , "energy" : 0, "fulfillment" : 0, "social": 0 },
                   "shy": {"hunger" : 0 , "energy" : 0, "fulfillment" : 0 , "social": 2},
                   "affectionate" : { "hunger" : 0, "energy" : 0, "fufillment" : 1, "social" : -1},
                   "playful": {"hunger": 0, "energy" : 1, "fulfillment" : 1 , "social" : 0},
                   "curious" : {"hunger" : 0, "energy": 1, "fulfillment": -1, "social": 0},
                   "grumpy": { "hunger" : 0, "energy": 0, "fulfillment" : 2, "social" : 1},
                   "adventourous" : {"hunger" : 2, "energy" : 1, "fulfillment" : 1, "social" : 1},
                   "spoilt": { "hunger" : 0, "energy": -1, "fulfillment" : 2, "social" : 1}
                   }
#-----------------------------------------
# Classes
#-----------------------------------------

class Cat:
    def __init__(self, name, breed, owner, age):
        self.name = name     # Stores the name of the cat 
        self.breed = breed   #Stores the breed of the cat
        self.owner = owner   # Stores the name of the cat's owner
        self.age = age       # Stores the age of the cat
        
        self.trait = random.sample(list(trait_modifier.keys()), 3)  # generates 3 base traits for each catch from list
        self.social = 8             # stores the social fufillment level of cat
        self.hunger = 8             # stores the health level of the cat 
        self.energy = 8             # stores the energy level of cat
        self.fufillment = 8          # stores  the fufillment of cat 
        self.current_action = "sleeping" # states the current action the cat is doing
        
        self.current_mood = self.calculate_mood()   # states the current emotion cat feeling
#-----------------------------------------
#Methods
#----------------------------------------
# These our the actions that the cat can perform        
    
    # This method allow the cat to purr 
    def calculate_mood(self): 
            # Finds the lowest stats to dicatte what the cat is currenty feeling
            lowest_stat = min(self.hunger , self.energy, self.fufillment,self.social)
            
            if   lowest_stat <= 2:
                return "angry"
            elif lowest_stat <= 5:
                return "grumpy"
            elif lowest_stat <= 7:
                return "normal"
            else:
                return "happy"
    
    # this method calculates the cats stats as the day progress        
    def pass_time(self):
        # Base decay eveyr day
         hunger_drop = 1   
         energy_drop = 1
         fufillment_drop = 1
         social_drop = 1
        
        # loops through the traits of the cat and their dictioanry moddifier
         for trait in self.trait:
             mods = trait_modifier[trait]
             hunger_drop += mods["hunger"]
             energy_drop += mods ["eenrgy"]
             fufillment_drop += mods["fulfillment"]
             social_drop += mods["social"]
        
        # applys decay and prevents the stats from dropping below 0
         self.hunger = max(0, self.hunger - hunger_drop)
         self.energy = max(0, self.energy - energy_drop)
         self.energy = max(0, self.fufillment - fufillment_drop)
         self.social = max(0, self.social - social_drop) 
         
    def check_current_action(self):
        hunger = self.hunger
        energy = self.energy
        lowest_stat = min(self.hunger, self.social, self.fufillment, self.energy,)
           
    # This tells you about the cats profile or background
    def identity(self):
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
    cat_breed = input ("What is the breed of the cat ?")
    cat_owner = user_name
    cat_age = int(input("What is the age of the cat ? "))
    
    new_cat_profile = Cat (cat_name, cat_breed, cat_owner, cat_age)
    cat_profile.append(new_cat_profile) # adds the new cat profile to the bottom of the list of our cat proiles       
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