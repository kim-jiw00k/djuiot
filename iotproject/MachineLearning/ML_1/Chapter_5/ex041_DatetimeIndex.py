import pandas as pd

dates = ["2025-03-19", "2025/03/19", "03/19/2025", "03-19-2025"]
years = pd.DatetimeIndex(dates).year
print(years)
days = pd.DatetimeIndex(dates).day
print(days)
months = pd.DatetimeIndex(dates).month
print(months)

times = ["03/19/2025 14:20:15","03-19-2025 14:20:10","2025-03-19 14:20:15"]
hours = pd.DatetimeIndex(times).hour
print(hours)
