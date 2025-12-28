# to ask user 3 favourite movies and store in a list 
movie=[]
movie.append(input("enter first fav movie:"))
movie.append(input("enter second fav movie:"))
movie.append(input("enter third fav movie:"))
print(movie)


# to check if the list contains a palindrome of element 
num =[1,2,3,3,2,1]
num2=num.copy()
num.reverse()
if(num==num2):
    print("list is palindrome")
else:
    print("list is not palindrome")