# using continue(mainly used to skip any part)
num = 0
while num<=7 :
    if(num==4) :
        num+=1
        continue
    print(num)
    num+=1

#print only odd number till 12
print("odd numbers till 12 are")
i = 0
while i<=12 :
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1