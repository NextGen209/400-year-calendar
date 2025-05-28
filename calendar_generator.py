# ==== calendar_generator.py ====
import math

class Calendar400Years:
    # Checks if a year is a leap year
    @staticmethod
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Returns number of days in a month for a specific year
    @staticmethod
    def days_in_month(month, year):
        if month == 1: return 31
        elif month == 2: return 29 if Calendar400Years.is_leap(year) else 28
        elif month == 3: return 31
        elif month == 4: return 30
        elif month == 5: return 31
        elif month == 6: return 30
        elif month == 7: return 31
        elif month == 8: return 31
        elif month == 9: return 30
        elif month == 10: return 31
        elif month == 11: return 30
        elif month == 12: return 31
        else: return 0

    # Generates a visual calendar for a month
    @staticmethod
    def build_month_display(month, year):
        lines = []
        month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        # Header: "2025 May"
        lines.append(f"{year} {month_names[month - 1]}".ljust(22))
        lines.append("Su Mo Tu We Th Fr Sa")

        days = Calendar400Years.days_in_month(month, year)
        start_day = Calendar400Years.get_day_of_week(1, month, year)

        week = ' ' * (start_day * 3)
        day_index = start_day

        for date in range(1, days + 1):
            week += f"{date:2} "
            day_index += 1

            if day_index == 7:
                lines.append(week.rstrip())
                week = ""
                day_index = 0

        if week:
            lines.append(week.rstrip())

        return lines

    # Zeller's Congruence to find day of week (0 = Sunday, ..., 6 = Saturday)
    @staticmethod
    def get_day_of_week(day, month, year):
        if month < 3:
            month += 12
            year -= 1

        k = year % 100
        j = year // 100

        h = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) + (5 * j)) % 7
        return (h + 6) % 7

    # Main method: prints calendar from 1900 to 2300
    @staticmethod
    def main():
        for year in range(1900, 2301):
            year_title = f"============================== YEAR {year} =============================="
            print(f"\n{year_title.center(105)}\n")

            for group in range(0, 12, 3):  # 3 months per row
                quarter = []

                for m in range(3):
                    month = group + m + 1
                    quarter.append(Calendar400Years.build_month_display(month, year))

                max_lines = max(len(month) for month in quarter)

                # Print each line from 3 months with 35-char spacing
                for line in range(max_lines):
                    for m in range(3):
                        if line < len(quarter[m]):
                            print(quarter[m][line].ljust(35), end='')
                        else:
                            print(' ' * 35, end='')
                    print()

                print()  # space between month rows

# Call the main method to execute
Calendar400Years.main()
