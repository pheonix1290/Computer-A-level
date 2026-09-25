#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      annabel ene
#
# Created:     21/09/2026
# Copyright:   (c) annabel ene 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

def main():
   score = int(input("Enter your score"))
   match score:
    case a if -1 <= a < 2:
        print("A mark of ", score, "is U")
    case b if 2 <= b < 4 :
        print("A mark of" , score , "is grade 1")
    case c if 4 <= c < 13 :
        print("A mark of" , score , "is grade 2")
    case d if 13 <= d < 22 :
        print("A mark of" , score , "is grade 3")
    case e if 22 <= e < 31 :
        print("A mark of" , score , "is grade 4")
    case f if 31 <= f < 41 :
        print("A mark of" , score , "is grade 5")
    case g if 41<= g < 54 :
        print("A mark of" , score , "is grade 6")
    case h if 54 <= h < 67 :

        print("A mark of" , score , "is grade 7")
    case i if 67 <= i < 80 :
        print("A mark of" , score , "is grade 8")
    case j if j >= 80 :
        print("A mark of", score , "is grade 8. You our the goat")
    case _:
        print("Invalid score or score too low to garde,<''>you should be ashamed of yourself")

if __name__ == '__main__':
    main()
