a= int(input("enter number a:"))
b= int(input("enter number b:"))
c= int(input("enter number c:"))
if(a>=b and a>=c):
    print("largest number is a")
elif(b>=c and b>=a):
    print("largest number is b")
else:
    print("largest number is c")
