#Date Detection
#Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, 
#the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.
#The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021.

#Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September,
#and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years.
#Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
#Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
import re

def date_detection(date):
    date_regex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    date_match = date_regex.search(date)
    if date_match:
        day, month, year = date_match.groups()
        if int(month) in [4, 6, 9, 11] and int(day) > 30:
            return False
        elif int(month) == 2 and int(day) > 29:
            return False
        elif int(month) == 2 and int(day) == 29 and (int(year) % 4 != 0 or (int(year) % 100 == 0 and int(year) % 400 != 0)):
            return False
        elif int(month) not in [1, 3, 5, 7, 8, 10, 12] and int(day) > 31:
            return False
        else:
            return True
    else:
        return False
    
print(date_detection('31/02/2020')) # False
print(date_detection('31/04/2021')) # False
print(date_detection('29/02/2020')) # True
print(date_detection('29/02/2021')) # False