
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year_to_calculate = 2024
year_to_type = is_year_leap(year_to_calculate)

print(f'год {year_to_calculate}: {year_to_type}')
