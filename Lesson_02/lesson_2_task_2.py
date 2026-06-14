def is_year_leap(year):
    return True if year % 4 == 0 else False

year_num = int(input("Введите номер года: "))
result = is_year_leap(year_num)
print(f"Год {year_num}: {result}")