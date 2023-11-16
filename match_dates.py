import re

dates = input()

dates_regex = r"[0-3][0-9]/[A-Z][a-z]{2}/\d{4}|[0-3][0-9]-[A-Z][a-z]{2}-\d{4}|[0-3][0-9]\.[A-Z][a-z]{2}\.\d{4}"

found_dates = re.findall(dates_regex, dates)
for date in found_dates:
    print(f"Day: {date[0:2]}, Month: {date[3:6]}, Year: {date[7:11]}")
