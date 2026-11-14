## BUG 1:
- ran into a bug that caused my nested if..elif statements not to work 
- the bug had to do with attribute or string, where:
     if drop_cat_off.lower() == "yes" or "y":

 - the n was an empty string and becaused of that python run it to be true all the time  even when it false.
# Solution:
  1. use 'in' method and put response in a list:
     if drop_cat_off.lower() in ["no", "n"]:  

  2. use  'or' correctly:
    if drop_cat_off.lower() == "yes" or  drop_cat_off.lower() == "y":  