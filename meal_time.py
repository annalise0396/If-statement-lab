def main():
    user_time = input("enter 12-hour time (ex 8:30 PM): ").strip()
    converted_time = convert(user_time) 
    
    if converted_time is None:
        print("Invalid")
        return
    if 7.0 <= converted_time <= 8.0:
        print("Breakfast time!")
    elif 12.0 <= converted_time <= 13.0:
        print("Time for lunch!")
    elif 18.0 <= converted_time <= 19.0:
        print("Dinnertime!")
    else:
        print("It isn't time to eat right now.")

def convert(time):
    try:
        time_part, period = time.split()
        hours, minutes = map(int, time_part.split(":"))
        period = period.upper()
        

        if period == "PM" and hours != 12:
            hours += 12
        elif period == "AM" and hours == 12:
            hours = 0
            
        return hours + (minutes / 60.0)
    except ValueError:
        return None

if __name__ == "__main__":
    main()

    
