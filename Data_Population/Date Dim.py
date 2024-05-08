import random
import string
from datetime import datetime, timedelta

def generate_date_key(date):
    return int(date.strftime('%Y%m%d'))

def generate_date_dim():
    with open('Populate_Date.SQL', 'w') as data:
        current_date = datetime(2010, 1, 1)
        end_date = datetime(2025, 12, 31)  # End of 2025

        while current_date <= end_date:
            date_key = generate_date_key(current_date)
            date_ = current_date.strftime('%Y-%m-%d')
            day_of_week = current_date.strftime('%A')
            day_number_in_epoch = (current_date - datetime(1970, 1, 1)).days + 1
            week_number_in_epoch = (current_date - datetime(1970, 1, 1)).days // 7 + 1
            month_number_in_epoch = (current_date.year - 1970) * 12 + current_date.month
            day_number_in_calendar_month = current_date.day
            day_number_in_calendar_year = current_date.timetuple().tm_yday
            
            next_month = current_date.month + 1 if current_date.month < 12 else 1
            next_month_year = current_date.year + 1 if current_date.month == 12 else current_date.year
            
            fiscal_last_day_ind = 'Y' if (current_date.replace(day=1) + timedelta(days=32 - current_date.day)).month == next_month and (current_date.replace(day=1) + timedelta(days=32 - current_date.day)).year == next_month_year else 'N'
            
            calendar_month = current_date.strftime('%B')
            calendar_month_number_in_year = current_date.month
            calendar_year_month = current_date.strftime('%Y-%m')
            calendar_quarter = str((current_date.month - 1) // 3 + 1)
            calendar_year_quarter = current_date.strftime('%Y-Q') + calendar_quarter
            calendar_year = current_date.year
            fiscal_month = 'Q' + str((current_date.month - 1) // 3 + 1)
            fiscal_month_number_in_year = current_date.month
            fiscal_year_month = str(current_date.year) + '-' + fiscal_month
            fiscal_quarter = str((current_date.month - 1) // 3 + 1)
            fiscal_year_quarter = str(current_date.year) + '-Q' + fiscal_quarter
            fiscal_year = current_date.year + 1 if current_date.month >= 10 else current_date.year

            insert_statement = (
                f"INSERT INTO Date_Dim (Date_Key, Date_, Day_of_Week, Day_Number_in_Epoch, Week_Number_in_Epoch, "
                f"Month_Number_in_Epoch, Day_Number_in_Calendar_Month, Day_Number_in_Calendar_Year, Fiscal_Last_Day_Ind, "
                f"Calendar_Month, Calendar_Month_Number_in_Year, Calendar_Year_Month, Calendar_Quarter, "
                f"Calendar_Year_Quarter, Calendar_Year, Fiscal_Month, Fiscal_Month_Number_in_Year, Fiscal_Year_Month, "
                f"Fiscal_Quarter, Fiscal_Year_Quarter, Fiscal_Year) "
                f"VALUES ({date_key}, TO_DATE('{date_}', 'YYYY-MM-DD'), '{day_of_week}', {day_number_in_epoch}, {week_number_in_epoch}, "
                f"{month_number_in_epoch}, {day_number_in_calendar_month}, {day_number_in_calendar_year}, '{fiscal_last_day_ind}', "
                f"'{calendar_month}', {calendar_month_number_in_year}, '{calendar_year_month}', '{calendar_quarter}', "
                f"'{calendar_year_quarter}', {calendar_year}, '{fiscal_month}', {fiscal_month_number_in_year}, "
                f"'{fiscal_year_month}', '{fiscal_quarter}', '{fiscal_year_quarter}', {fiscal_year});\n"
            )
            data.write(insert_statement)
            
            current_date += timedelta(days=1)

generate_date_dim()


