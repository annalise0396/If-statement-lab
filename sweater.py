temp_input = input("What is the high temperature today? ").strip()

try:
    high_temp = int(temp_input)
    
    if high_temp <= 60:
        print("You need a sweater")
    elif 60 < high_temp < 140:
        print("You do not need a sweater")
    else:
        print("Invalid input")
        
except ValueError:
    print("Invalid input")



