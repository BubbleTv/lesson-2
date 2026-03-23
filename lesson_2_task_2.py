def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year1 = 2024
result1 = is_year_leap(year1)
print(f"год {year1}: {result1}")

year2 = 2025
result2 = is_year_leap(year2)
print(f"год {year2}: {result2}")

year3 = 2000
result3 = is_year_leap(year3)
print(f"год {year3}: {result3}")

year4 = 2026
result4 = is_year_leap(year4)
print(f"год {year4}: {result4}")