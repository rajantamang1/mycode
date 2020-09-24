def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def sub(a,b):
    return  a-b

def div(a,b):
    return a/b

def main():
    try:
        input1 = float(input("Enter first number: "))
        input2 = float(input("Enter second number: "))
        input3 = input("Select: add,subtract, divide, multiply: ").lower()
    
        if (input3 == "add"):
            print("The sum is", add(input1, input2))
        elif (input3 == "subtract"):
            print("The subtract is", sub(input1, input2))
        elif (input3 =="divide"):
            print("The division is",div(input1,input2))
        elif (input3== "multiply"):
            print("The multiple is",multiply(input1, input2))
    except:
        print("No valid input")
        main()

main()