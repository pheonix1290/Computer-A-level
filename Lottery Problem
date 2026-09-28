import random
number = [random.randint(1,31) for _ in range(3)]

guess = []
count = 1

while len(guess) < 3:
    num = int(input(f"enter your guess {count} between 1-30:"))
    if 1<= num <= 30:
        guess.append(num)
        count += 1
    else:
        print("try again")   

if guess == number:
    print("you win")
else:
    print(f"you lose, the correct numbers were {number}") 
    print(f"your guess was {guess}")  