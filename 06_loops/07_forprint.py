#print elemets using for loop 
ele = [1,4,9,16,2,36,49,81,100]
for numb in ele:
    print(numb)

#searching number x in the tup
num = (1,4,9,16,25,36,49,81,100)
x=int(input("enter number x:"))
i=0
for elem in num:
    if(elem==x):
        print("number found at index",i)
        break
    i+=1
else:
    print("number not found")
