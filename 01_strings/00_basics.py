#concatenation is adding strings
#\n plays same role as in C, changes the line
str1 = "2026"
str2 = "will be Great"
print(str1+" "+str2)

#len function can be used to determine the length of the string {spaces also count in the len}
print(len(str1))
print(len(str2))

#indexing starts from 0 and can be accessed as str[]
print(str2[5])

#slicing is concept to cut or to take specific part of a string
#in str[a:b] a is included while b is not included
print(str2[1 : 7]) 
print(str2[:6]) #[0:6]
print(str2[3:]) #[3:len(str2)]