# range is a function which returns sequence of numbers, starting from 0 by default 
# and incrememts by 1 by default, they stops before a specified numbers.
seque = range(5)
print(seque[0])
print(seque[1])
print(seque[2])
print(seque[3])
print(seque[4])
for seq in seque:
    print(seq)

#methods to define 
for i in range(4): #range(stop)
      print(i) 
for i in range(1,4): #range(start,stop)
     print(i)
for i in range(2,7,2): #range(start,stop,stepup)
     print(i)