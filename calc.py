def calculate():
    user_input = input("Enter a calculation: ")
  
    parts = user_input.split()
    
    if len(parts) != 3:
        print("enter the calculation with spaces")
        return

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("invalid")
            return
        result = num1 / num2
    else:
        print("error")
        return
        
    print(f"result: {result}")

calculate()


