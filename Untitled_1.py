'''

for i in range(1,3):
    for j in range(2):
        print(i,j)


i,j = 0,1
while i <4:
    while j<5:
        print(i,j)
        i+=1
        j+=1


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
'''
l = [1,2,3,4]
l.append(5)
l.
print(l)