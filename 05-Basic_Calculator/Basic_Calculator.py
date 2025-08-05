while True :
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    op = input("Enter operator : ")

    if op == "+":
        print(num1, op, num2, " = ", num1 + num2)
    elif op == "-":
        print(num1, op, num2, " = ", num1 - num2)
    elif op == "*":
        print(num1, op, num2, " = ", num1 * num2)
    elif op == "/":
        try:
            print(num1, op, num2, " = ", num1 / num2)
        except ZeroDivisionError:
            print("Division by zero not possible.")
    else:
        print("Invalid Operator ")
    cont = input("Enter 0 to exit\n")
    if cont=="0" :
        break