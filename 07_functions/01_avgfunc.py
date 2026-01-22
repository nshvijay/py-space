# create a fucntion which give avg of 3 numbers
def avg_3(a,b,c):
    avg=(a+b+c)/3
    return avg

print("For average of 3 numbers.")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
print("Average is ",avg_3(a,b,c))
