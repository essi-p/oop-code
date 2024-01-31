from datetime import date

def list_years(dates: list):
    years = [d.year for d in dates]
    sorted_years = sorted(set(years))
    return sorted_years

date_list = [date(2020, 5, 15), date(2018, 8, 23), date(2019, 12, 10), date(2020, 1, 5)]

result = list_years(date_list)
print(result)
