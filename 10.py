def get_astrological_sign(day, month):
    zodiac_signs = {
        'capricorn': ((12, 22), (1, 19)),
        'aquarius': ((1, 20), (2, 18)),
        'pisces': ((2, 19), (3, 20)),
        'aries': ((3, 21), (4, 19)),
        'taurus': ((4, 20), (5, 20)),
        'gemini': ((5, 21), (6, 20)),
        'cancer': ((6, 21), (7, 22)),
        'leo': ((7, 23), (8, 22)),
        'virgo': ((8, 23), (9, 22)),
        'libra': ((9, 23), (10, 22)),
        'scorpio': ((10, 23), (11, 21)),
        'sagittarius': ((11, 22), (12, 21)),
        'capricorn': ((12, 22), (1, 19))
    }

    month = month.lower()

    month_names = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    
    month_number = month_names.get(month)

    if month_number is None:
        return "Invalid month name."

    for sign, ((start_month, start_day), (end_month, end_day)) in zodiac_signs.items():
        if (month_number == start_month and day >= start_day) or (month_number == end_month and day <= end_day):
            return sign.capitalize()
    
    return "Invalid date."

day = int(input("Input birthday: "))
month = input("Input month of birth (e.g. march, july etc): ")

astrological_sign = get_astrological_sign(day, month)
print(f"Your Astrological sign is: {astrological_sign}")
