#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      annabel ene
#
# Created:     28/09/2026
# Copyright:   (c) annabel ene 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

def main():
    car_year = int(input("what is the year of your car?"))
    car_value = float(input("What the value of teh car"))
    resale_value = float(input("What the minimum resale value of the car"))

    year_pased = 0

    while car_value >= resale_value:
        print(f"{car_year} : {int(car_value)}")

        car_year += 1

        if year_pased > 2:
            rate = 0.30
        else:
            rate = 0.20

        new_value = car_value * (1 - rate)
        car_value = new_value
        print(f"{car_year} : {int(new_value)}")
        if new_value > resale_value:
            print(f"part echnage in {car_year}")
        break





if __name__ == '__main__':
    main()
