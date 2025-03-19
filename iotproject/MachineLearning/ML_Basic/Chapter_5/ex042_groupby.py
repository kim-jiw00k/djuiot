import pandas as pd
weather_data = 'https://github.com/dongupak/DataML/raw/main/csv/weather.csv'
print(weather_data)
weather = pd.read_csv(weather_data, encoding='CP949') # encoding='CP949' 한글 사용 하기 위한 것
print(weather)
print(weather.head())
print(type(weather))
weather['Month'] = pd.DatetimeIndex(weather['일시']).month
print(weather)
monthly_means = weather.groupby('Month')[['평균기온','최대풍속','평균풍속']].mean()
print(monthly_means)