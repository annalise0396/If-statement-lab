leap_year = int(input("What year is it?").strip())

if leap_year%400==0:
    print("leap year")
elif leap_year%100==0:
    print("not leap year")
elif leap_year%4==0:
    print("leap year")
else:
    print("not a leap year")
