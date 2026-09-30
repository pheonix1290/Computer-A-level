notes = int(input("How much money do you want to redraw?"))

print(f"Withdraw: ${notes}")

remain = notes
# it will dispense 20 notes until remain is less than 20
while remain >= 20:
    print("Dispense $20")
    remain -= 20
# it will dispense 10 notes until remian is less than 10    
while remain >= 10:
    print("Dispense $10")
    remain -= 10
#it will dispense 5 notes until remain is less tahn 5    
while remain >= 5:
    print("Dispense $5")
    remain -= 5
if remain > 0:
    print(f"Sorry couldn't depense the remaining ${remain}. Only have $5, $10 and $20 notes")
else: 
    print()