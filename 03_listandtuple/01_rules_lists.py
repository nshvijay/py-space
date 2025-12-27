#strings and lists are similar but difference of changeability
str="Vijay"
print(str[1])
# "str[1]=y" this will show error as not allowed for strings

us =["me","oneday","wait","7years","future","dreams","success"]

print(us[3])
us[3]="ready"
print(us[3]) #here "7years" is replaced by "ready" as its allowed for lists.

#this happens because lists are mutable while strings are inmutable 
print(us)

#slicing is also possible in lists