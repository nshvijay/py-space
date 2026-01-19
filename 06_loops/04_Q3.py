#printing list's element using loop
num =[1,4,9,16,25,36,49,64,81,100]
i = 0
while i<=(len(num)-1) :
    print(num[i])
    i+=1

# finding index of number x
arr =(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter number:"))
j=0
while j<=(len(arr)-1) :
    if(arr[j]==x):
        print("number found at index",j)
        break
    j+=1
else:
        print("number not found")

