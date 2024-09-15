def find_season(month, day):
    if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day < 20):
        season = "winter"
    elif (month == 3 and day >= 20) or (4 <= month <= 5) or (month == 6 and day < 21):
        season = "spring"
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day < 22):
        season = "summer"
    elif (month == 9 and day >= 22) or (10 <= month <= 11) or (month == 12 and day < 21):
        season = "autumn"
    
    return season

month = int(input("Input the month (e.g. [1-12]): "))
day = int(input("Input the day: "))


month_names = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]

if 1 <= month <= 12 and 1 <= day <= 31:  
    month_name = month_names[month - 1]
    season = find_season(month, day)
    print(f"{month_name}, {day}. Season is {season}")
else:
    print("Invalid month or day input")