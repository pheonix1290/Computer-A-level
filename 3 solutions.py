def cal(a,b):
    constant_val = 2
    x = constant_val * (a + b)
    y = a - b
    z = a * b
    return x,y,z
def main():
  a = int(input("Type in a random number you want to add,subtract,multiply"))
  b = int(input("Type in a second one"))

  add, subtract ,multiply = cal(a,b)
  print(add, subtract , multiply)