#so here in python input work as printf to show and scanf to accept value as in C, both combined
name = input("enter your name:")
age = input("enter your age")
print("Hello!",name)
print("your age is",age)
#the type of every input is always a string
print(type(age))#type is str even age is a int

#to avoid that typecasting can be used
price=float(input("enter price of ball:"))
print(type(price))

#input 2 numbers and print their sum
num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
print(num1+num2)

