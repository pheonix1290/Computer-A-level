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
def get_conversation():
    GBP = 100
    currency_name = input("Which currency do you want to exchange to from the given option ?")
    if currency_name == "USD":
            USD = GBP * 1.25
            print("100 GBP =" , USD )
    elif currency_name == "Euro" :
            Euro = GBP * 1.03
            print("100 GBP = " , Euro )
    elif currency_name == "Yen" :
            Yen = GBP * 210.39
            print("100 GBP = " , Yen )
    elif currency_name == "Yuan":
            Yuan = GBP * 8.96
            print("100 GBP = " , Yuan)
    else:
        print("Sorry but we don't have your currency. Please kindly look somewhere else")
def main():
    print("Hi,")
    GBP = 100
    pound = input("Do you want to know the exchange rate for pounds to USD, EURO,Yuan and Yen yes/no")

    if pound == "yes":
        currency_name = input("Which currency do you want to exchange to from the given option ?")
        if currency_name == "USD":
            USD = GBP * 1.25
            print("100 GBP =" , USD )
        elif currency_name == "Euro" :
            Euro = GBP * 1.03
            print("100 GBP = " , Euro )
        elif currency_name == "Yen" :
            Yen = GBP * 210.39
            print("100 GBP = " , Yen )
        elif currency_name == "Yuan":
            Yuan = GBP * 8.96
            print("100 GBP = " , Yuan)
        else:
            print("Sorry but we don't have your currency. Please kindly look somewhere else")
    elif pound == "no":
        response = input("Our you sure ,if so press enter, if you change your mind enter yes")
        if response == "yes":
                get_conversation()
        else:
            print("Sorry look somewhere else")
    else :
        print("Sorry we can't help you")
if __name__ == '__main__':
    main()
