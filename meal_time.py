time_str = input("What time is it? (HH:MM), 24 hour clock: ")
hours, minutes = map(int, time_str.split(":"))
decimal_hours = hours + (minutes / 60)

if 7 <= decimal_hours <= 8:
    print("Breakfast time!")
elif 12 <= decimal_hours <= 13:
    print("Time for lunch!")
elif 18 <= decimal_hours <= 19:
    print("Dinnertime!")
else:
    print("It isn't time to eat right now.")

    
