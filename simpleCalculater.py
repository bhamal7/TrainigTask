# Simple code to find a calculater

#First I will define a functions

def add(first,second):
    return first+second

def subtract(first,second):
    return first-second

def multiply(first,second):
    return first*second

def divide(first,second):
    return first/second


while True:  
    option=input("Enter the options: \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n ")
  
    if option in ('1','2','3','4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

   
        if option == '1':
            print(num1,' + ',num2,' is ',add(num1,num2))
        elif option == '2':
            print(num1, " - ",num2, ' is ',subtract(num1,num2))
        elif option == '3':
            print(num1," x ",num2," is ",multiply(num1,num2))
        elif option == '4':
            print(num1,' / ',num2, ' is ',divide(num1,num2))
    
        next = input("Want to do next calculation: Enter Yes or no: ")
        if next =='no':
            print("Done!")
            break
    else:
        print("Please enter options 1-4.")
