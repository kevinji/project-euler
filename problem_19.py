'''
Problem 19

@author: Kevin Ji
'''


class Date:
    # Class
    DAYS_OF_WEEK = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}

    MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    @staticmethod
    def is_leap_year(year):
        return True if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else False

    @staticmethod
    def get_month_num(month):
        return Date.MONTHS[month]

    @staticmethod
    def get_days_in_month(year, month):
        month_num = Date.get_month_num(month) if isinstance(month, str) else month

        # 29 days in February in a leap year
        if Date.is_leap_year(year) and month_num == Date.get_month_num("Feb"):
            return 29

        return Date.DAYS_IN_MONTH[month_num]

    @staticmethod
    def is_sunday(day_of_week):
        return True if day_of_week % 7 == 0 else False

    @staticmethod
    def get_num_sundays(date_from, date_to):
        num_sundays = 0

        day = date_from.day
        month = date_from.month
        year = date_from.year
        day_of_week = date_from.day_of_week

        while year <= date_to.year:
            # Go to December if it's not the last year
            if year < date_to.year:
                month_end = Date.get_month_num("Dec")
            else:
                month_end = date_to.month

            while month <= month_end:
                days_in_month = Date.get_days_in_month(year, month)

                while day <= days_in_month:
                    if Date.is_sunday(day_of_week):
                        num_sundays += 1

                    day += 1
                    day_of_week += 1

                # Cleanup after every month
                day = 1
                month += 1

            # Cleanup after every year
            month = Date.get_month_num("Jan")
            year += 1

        return num_sundays

    @staticmethod
    def get_num_sundays_on_first_of_month(date_from, date_to):
        num_sundays = 0

        day = date_from.day
        month = date_from.month
        year = date_from.year
        day_of_week = date_from.day_of_week

        while year <= date_to.year:
            # Go to December if it's not the last year
            if year < date_to.year:
                month_end = Date.get_month_num("Dec")
            else:
                month_end = date_to.month

            while month <= month_end:
                days_in_month = Date.get_days_in_month(year, month)

                while day <= days_in_month:
                    if Date.is_sunday(day_of_week) and day == 1:
                        num_sundays += 1

                    day += 1
                    day_of_week += 1

                # Cleanup after every month
                day = 1
                month += 1

            # Cleanup after every year
            month = Date.get_month_num("Jan")
            year += 1

        return num_sundays

    # Object
    def __init__(self, year, month, day, day_of_week):
        self.year = year
        self.month = Date.get_month_num(month)
        self.day = day
        self.day_of_week = Date.DAYS_OF_WEEK[day_of_week]


begin_date = Date(1901, "Jan", 1, "Tue")
end_date = Date(2000, "Dec", 31, "Sun")

print("The number of Sundays on a first of a month is equal to:")
print(Date.get_num_sundays_on_first_of_month(begin_date, end_date))
