#---------------------------------------------------------------------------------------
# Name:        month matcher
# Purpose:
#
# Author:      annabel ene
#
# Created:     02/10/2026
# Copyright:   (c) annabel ene 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------
def month_data():
    month_data =[
               {"month" : "January" , "no_days": 31 , "no_month" : 1},
               {"month" : "Feburary" , "no_days": 28 , "no_month" : 2},
               {"month" : "March", "no_days" : 31 , "no_month" : 3},
               {"month" : "April" , "no_days": 30, "no_month": 4},
               {"month" : "May" , "no_days": 31 , "no_month" : 5},
               {"month" : "June" , "no_days": 30 , "no_month" : 6},
               {"month" : "July" , "no_days" : 31 , "no_month" :7 },
               {"month" : "August" , "no_days" : 31 , "no_month" : 8},
               {"month" : "September" , "no_days" : 30 , "no_month" : 9},
               {"month" : "October" , "no_days" : 31 , "no_month" : 10},
               {"month" : "November" , "no_days" : 30 , "no_month" : 11},
               { "month" : "December" , "no_days" : 31 , "no_month" : 12}
            ]
def main():
# These is a dictionary containing information based on month and number of days within it

 #use state whether loop would run or stop
 is_running = True
 while is_running:
    choice = input("Do you want to 'search' what it be in a month time or 'close' ").strip().lower()
    # decided what happens is the user input 'search' or 'close'
    if choice == "close":
        is_running = False
    elif choice == "search":
        a = int(input("type in number of the day"))
        b = input("type in a month or the position the month is in the year").strip().capitalize()
      # converts user_input of b to an integer  if it a number
        if b.isdigit():
            b = int(b)
            # matching the users input for b, by checking the rows withing my dictionary for the key with that number
            for row in month_data:
                match row:
                   case{"month" : m_name , "no_month": m_num }:
                       if m_num == b:
                          b = m_name
                          break
            print(f"{b} {a} ina month time it would be...")
        print(f"From {b} {a} in a month time it would be ...")
        # turning b back to a number
        if type(b) == str:

            b = b.strip().title()
            for row in month_data:
                match row:
                    case{"no_month": m_num, "month" : m_name }:
                        if b == m_name:
                            b = m_num
                            break

        ans = b
        while ans == b :
            for row in month_data:
                match row:
                    case{"no_days" : num_days , "no_month" : b }:
                        days_left = num_days - a
                        ans  = 30 - days_left
                        b += 1
                        break
             # converts back to name
            if type(b) == int:
                for row in month_data:
                    match row:
                        case{"month": name, "no_month": num}:
                            if num == b:
                                b = name
                                break
    print(f"{b} {a}")





if __name__ == '__main__':
    main()
