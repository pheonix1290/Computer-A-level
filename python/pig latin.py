vowels = ["a" , "e" , "i", "o" , "u"]




# ----------------------------------------
# Subprogram
# ---------------------------------------
def pig_laten_converter(lang):

            if lang[0].lower() in vowels:
                text_vol = lang + "yay"
                return text_vol
            elif not (lang[0].lower() in vowels ):
               whole_lang = lang[1:]
               lang_con = lang[:1]
               text = whole_lang+ lang_con + "ay"
               return text
# ----------------------------------------
# Main program
# ---------------------------------------




def main():
       print("Hi Hello Welcome to Pig Latin converter. Where you get to turn any english word to Pig latin !!")
       name = input("What is your name dear user \n")
       print(f"What a wonderful name ,{name} . Let's go")
       text = input("Type in any random text or word \n")
       eng_text = pig_laten_converter(text)
       print(eng_text)
main()



