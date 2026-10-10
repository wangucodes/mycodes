a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
t1, t2 = a, b
while b > 0:
    r = a % b
    a = b
    b = r
GCD= a
LCM = (t1 * t2) / GCD
print("GCD is", GCD)
print("LCM is", LCM)
