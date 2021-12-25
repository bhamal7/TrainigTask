print("For loop: ")
for i in range(1,3):
    for j in range(2):
        print(i,j)

print("while loop: ")
i,j = 0,1
while i <4:
    while j<5:
        print(i,j)
        i+=1
        j+=1

print("Function: ")
def welcome():
    x=10
    return x
  
welcome()    
print(type(welcome()))

x = "global"
def func():
    print(x)
func()  
print(x)
l = [1,2,3,4]
l.append(5)
print(l)

from functools import reduce

print("filter,map and reduce function using lambda function: ")
nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda i : i % 2 == 0,nums))
odds = list(filter(lambda i : i%2==1,nums))
print("evens are ",evens,"and odds are ",odds)

doubles = list(map(lambda i : i*2,nums))
print("The doubles of the list is ", doubles)

sum=reduce(lambda a,b: a+b,nums)
print("The sum of the given list is ",sum)

