
def addition(num1,num2):
    result = num1 + num2
    print("Result: ",num1,'+',num2,'=',result)

def subtraction(num1,num2):
    result = num1 - num2
    print("Result: ",num1,'-',num2,'=',result)

def multipication(num1,num2):
    result = num1 * num2
    print("Result: ",num1,'*',num2,'=',result)

def devition(num1,num2):
    while num2 == 0:
        print("You can't devided by the 'zero'")
        num2 = float(input("Please enter again you second number: "))

    resul = num1 / num2
    print("Result: ",num1,'/',num2,'=',resul)


#Display to user 

print("Wellcome to the calculator!")
while True:

    print("Type 1 if you want to addition'+'")
    print("Type 2 if you want to subtraction'-'")
    print("Type 3 if you wat to multipication'*'")
    print("Type 4 if you want to devition'/'")
    print("Type Y if you want to exit from calculator")
    
    choice = input("Enter your choice: ")
    if choice.lower() =="y":
        print("Thanks for using our calculator!")
        break
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))


    if choice =="1":
        addition(num1,num2)
        
    elif choice =="2":
        subtraction(num1,num2)

    elif choice =="3":
        multipication(num1,num2)
        
    elif choice =="4":
        devition(num1,num2)
    else:
        print("Invalid choice please try again ")


