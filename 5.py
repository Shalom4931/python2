def month_to_days(month):
    month_days = {
        "January": 31, "February": 28/29, "March": 31, "April": 30,
        "May": 31, "June": 30, "July": 31, "August": 31,
        "September": 30, "October": 31, "November": 30, "December": 31
    }
    
    

    if month in month_days:
        print(f"{month} has {month_days[month]} days.")
    else:
        print("Invalid month name.")

month_name = input("Enter the name of the month: ")
month_to_days(month_name)