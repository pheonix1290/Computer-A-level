
x = int(input("Input any value to find the root when using Newton's method"))
root = x
print(x)

while root * root != x:
    root = 0.5 * (root + (x/root))
    print(root)
    print("end")

