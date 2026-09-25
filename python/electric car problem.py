#---------------------------------------------------------------------------------------
# Name:        Electric Car Problem
# Purpose:
#
# Author:      annabel ene
#
# Created:     23/09/2026
# Copyright:   (c) annabel ene 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

def main():
 print("Hi")
 response = input("Do you want to know how much your cost is and the points you gained. yes/no")

 if response in ["yes", "y"]:
   minutes = int(input("What is the number of minutes you charged your vehicle for?"))

   if minutes < 15 :
        total_cost = 1 + (15 * 20 / 100)
        point_gain = int(1.5 * 15)
        print(f"The total cost of minutes you charged is ${total_cost} and the points gained is {point_gain}points")
   elif minutes >= 15 :
        total_cost = 1 +  (minutes * 20 / 100)
        point_gain = int(1.5 * minutes)
        print(f"The total cost of minutes you charged is ${total_cost} and the points gained  is {point_gain}points")
   else:
       print("Error!")
 else:
    print("Sorry can't help you")

if __name__ == '__main__':
    main()
