#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      annabel ene
#
# Created:     11/09/2026
# Copyright:   (c) annabel ene 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

def main():
 width = int(input("What id the width of the room?"))  # noqa: F841
length = int(input("What the length of the room?"))
carpert_price_per_m2 = int(input("What is the price for m2 of carpet ?"))

area = width * length
perimeter = (width * 2) + (length * 2)
carpet_cost = area * carpert_price_per_m2

underlay_cost = area * 3
grippers_cost = perimeter * 1
fitting_fee = 50

total_cost = carpet_cost + underlay_cost + grippers_cost + fitting_fee
print(f"Room dimensions : {width} x {length}m")
print(f"'Carpe Price: ${carpet_price_per_m2} per m2\n")
print(f"Carpet Cost: ${carpet_cost}")
print(f"Underlay Cost: ${underlay_cost}")
print(f"Grippers Cost: ${grippers_cost}")
print(f"Fitting Fee: ${fitting_fee}")
print("-" * 20)
print(f"Total Cost: ${total_cost}")
if __name__ == '__main__':
    main()
