earnings_per_hour = input('How much do you earn per hour? ')
work_hours_for_month = input('How many hours do you work per month? ')
earnings_per_hour_in_float = float(earnings_per_hour)
work_hours_for_month_in_float = float(work_hours_for_month)
earning_times_work_hours = earnings_per_hour_in_float * work_hours_for_month_in_float
print(f'You working {work_hours_for_month_in_float} hours per month earn {earning_times_work_hours} per month')