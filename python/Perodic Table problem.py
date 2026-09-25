#---------------------------------------------------------------------------------------
# Name:        Periodic Table problem
# Purpose:
#
# Author:      annabel ene
#
# Created:     23/09/2026
# Copyright:   (c) annabel ene 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

def main():
   element = input("Give me the name of any of the first 20 elements,the atomic mass or group it belongs too and I will tell you about them?")

   match element:

      # Group 1 elements

    case "H" | _ if element.lower() in ["h" , "hydrogen" , "1" , "group 1" , "alkali metals" ]:  # noqa: F841
        print("""
                 Element : Hyrdogen
                 Atomic Weight : 1
                 Atomic No : 1
                 Group: 1
                 Type of metal : Alkali """)
    case "Na" | _ if element.lower() in ["na" , "sodium" , "11" , "group 1", "22.99"] :  # noqa: F841
        print("""
                 Element: Sodium
                 Atomic weight: 22.99
                 Atomic No: 11
                 Group: 1
                 Type of metal : Alkali""")
    case "Li" | _ if element.lower() in ["li" , "lithium" , "3" , "group 1" ,"6.94"] :  # noqa: F841
        print("""
                 Element: Lithium
                 Atomic weight: 6.94
                 Atomic No: 3
                 Group: 1
                 Type of metal : Alkali""")
    case "K" | _ if element.lower() in ["k" , "potassium" , "19" , "group 1" , "39.09"] :  # noqa: F841
        print("""
                 Element: Potassium
                 Atomic weight: 39.09
                 Atomic N0: 19
                 Group: 1
                 Type of metal: Alkali""")

    # Group 2 elements
    case "Be" | _ if element.lower() in ["be" , "beryllium" , "4" , "group 0" , "9.012"] :
        print("""
                 Element: Beryllium
                 Atomic weight: 9.012
                 Atomic No: 4
                 Group: 0
                 Type of metal: Alkaline earth metals""")
    case "Mg" | _ if element.lower() in ["mg" , "magnesium" , "12" , "group 2" , "24.30"] :
        print("""
                 Element: Magnesium
                 Atomic weight: 24.30
                 Atomic No: 12
                 Group: 2
                 Type of metal: Alkaline earth metals""")
    case "Ca" | _ if element.lower() in ["ca" , "calcium" , "20" , "group 2" ,"40.07"] :
        print("""
                 Element: Calcium
                 Atomic Weight: 40.07
                 Atomic No: 20
                 Group: 2
                 Type of Metal: Alkaline earth metals""")
    case "He" | _ if element.lower() in ["he" , "helium" , "2" , "group 2" , "4.00" ] :
        print("""
                 Element:Helium
                 Atomic weight: 4.00
                 Atomic No: 2
                 Group: 2
                 Type of metal: Alkaline earth metals""")

    # Group 3 element
    case "B" | _ if element.lower() in ["b" , "boron" ,"5" , "group 3" , "11"] :
        print("""
                 Element: Boron
                 Atomic weight: 11
                 Atomic No: 5
                 Group: 3
                 Type of metal: Metalloids""")
    case "Al" | _ if element.lower() in ["al" , "aluminium" , "group 3" , "13", "27"] :
        print("""
                 Element: Aluminium
                 Atomic weight: 27
                 Atomic No: 13
                 Group: 3
                 Type of metal: Metalloids""")
    case "Ga" | _ if element. lower() in ["ga" , "gallium" , "group 3" , "31" , "70"] :
        print("""
                 Element: Gallium
                 Atomic Weight: 70
                 Atomic No: 31
                 Group: 3
                 Type of metal: Metalloids""")

    # Group 4 elements
    case "C" | _ if element.lower() in ["c" , "carbon" , "group 4" , "12" , "6"] :
        print("""
                 Element: Carbon
                 Atomic weight: 12
                 Atomic No: 6
                 Group: 4
                 Type of metal: Reactive non-metals""")
    case "Si" | _ if element.lower() in ["si" , "silicon" , "group 4" , "28" , "14" ] :
        print("""
                 Element: Silicon
                 Atomic weight: 28
                 Atomic No: 14
                 Group: 4
                 Type of metal: Metalloids""")
    case "Ge" | _ if element.lower() in ["ge" , "germanium" , "group 4", "73" , "32"] :
        print("""
                 Element: Germanium
                 Atomic weight: 73
                 Atomic No: 32
                 Group: 4
                 Type of metal: Metalloids""")

    # Group 5 elements

    case "N" | _ if element.lower() in ["n" , "nitrogen" , "group 5" , "7" , "14"]:
        print("""
                 Element: Nitrogen
                 Atomic weight: 14
                 Atomic No: 7
                 Group: 5
                 Type of metal: Reactive non-metals""")
    case "P" | _ if element.lower() in ["p" , "phosphorus" , "group 5" , "15" , "31" , "30.97"] :
        print("""
                 Element: Phosphorus
                 Atomic weight: 31
                 Atomic No: 15
                 Group: 5
                 Type of metal: Reactive non-metals""")
    case "As" | _ if element.lower() in ["as" , "Arsenic" , "group 5" , "75" , "33"] :
        print("""
                 Element: Arsenic
                 Atomic weight: 75
                 Atomic No: 33
                 Group: 5
                 Type of metal: Metalloids """)

    # Group 6 elements

    case "O"| _ if element.lower() in ["o" , "oxygen" , "16" , "8" , "15.99" , "group 6"] :
        print("""
                 Element: Oxygen
                 Atomic weight: 16
                 Atomic No: 8
                 Group: 6
                 Type of metal: reactive non-metal""")
    case "S" | _ if element.lower() in ["s" , "sulfur" , "32" , "16" , "32.06", "group 6"] :
        print("""
                 Element: Sulfur
                 Atomic weight: 32
                 Atomic No: 16
                 Group: 6
                 Type of metal: reactive non-metal""")
    case "Se" | _ if element. lower() in ["se" , "selenium" , "79" , "34" , "group 6", "78.97"] :
        print("""Element: Selenium
                 Atomic weight: 79
                 Atomic No: 34
                 Group: 6
                 Type of metal: reactive non-metal""")

    # Group 7 elements
    case "F" | _ if element.lower() in ["f" , "fluorine" , "19" , "9" , "group 7" , "18.99"] :
        print("""
                 Element: Fluorine
                 Atomic weight: 19
                 Atomic No: 9
                 Group: 7
                 Type of elements: reactive non-metal""")
    case "Cl" | _ if element.lower() in ["cl" , "chlorine" , "17" , "35.5" , "group 7" , "35.45"] :
        print("""Element: Chlorine
                 Atomic weight: 35.5
                 Atomic No: 17
                 Group: 7
                 Type of metal: reactive non-metal""")
    case "Br" | _ if element.lower() in ["br" , "bromine" , "80" , "35" , "group 7" , "79.90"] :
        print("""
                 Elements: Bromine
                 Atomic weight: 80
                 Atomic No: 35
                 Group: 7
                 Type of metal: reactive non-metal""")

    # Group o element
    case "Ne" | _ if element.lower() in ["ne" , "Neon" , "20" , "10", "group 0" , "20.18" ] :
        print("""
                 Element: Neon
                 Atomic Weight: 20
                 Atomic No: 10
                 Group: 0
                 Type of metal: Noble gas""")
    case "Ar" | _ if element.lower() in ["ar" , "argon" , "40","18" , "group 0" , "39.95" ] :  # noqa: F841
        print("""
                 Element: Argon
                 Atomic weight: 40
                 Atomic No: 18
                 Group: 0
                 Type of metal: Noble gas""")
    case "Kr" | _ if element.lower() in ["kr" , "krypton" , "84" , "36" , "group 0", "83,80"] :  # noqa: F841
        print("""
                 Element: Krypton
                 Atomic weight: 84
                 Atomic No: 36
                 Group: 0
                 Type of metal: Noble gas""")
if __name__ == '__main__':
    main()
