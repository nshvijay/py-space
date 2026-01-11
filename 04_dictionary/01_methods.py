student ={
    "name" : "vijay",
    "age"  : 18,
    "grade":  "A",
    "subjects":["maths","python","C++"]
    }
print(student.keys())     #prints all keys
print(student.values())   #prints all values
print(list(student.items()))    #prints all (key, value) tuples
print(student.get("name")) #gives value of the key 
print(len(student))
print(student.items())
print(student)
print(student["name"])