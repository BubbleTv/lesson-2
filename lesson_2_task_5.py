def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный номер месяца"
month1 = 2
result1 = month_to_season(month1)
print(f"Месяц {month1}: {result1}")

month2 = 5
result2 = month_to_season(month2)
print(f"Месяц {month2}: {result2}")

month3 = 7
result3 = month_to_season(month3)
print(f"Месяц {month3}: {result3}")

month4 = 10
result4 = month_to_season(month4)
print(f"Месяц {month4}: {result4}")

month5 = 13
result5 = month_to_season(month5)
print(f"Месяц {month5}: {result5}")