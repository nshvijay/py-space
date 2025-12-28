#tuple is also an data type
#can simply be described as immutable list

tup=(3,5,6,7,8,3) 
print(tup)
print(type(tup))
# tup[3]=5 this is not valid as tuples are immutable

# tuple methods 

print(tup.index(6))    #gives the index of first appreance 
print(tup.count(3))   #counts the number of appreance of that element 
