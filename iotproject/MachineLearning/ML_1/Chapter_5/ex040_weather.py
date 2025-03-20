import pandas as pd

weather_data = 'https://github.com/dongupak/DataML/raw/main/csv/weather.csv'
print(weather_data)

weather = pd.read_csv(weather_data, index_col=0,encoding='CP949') # encoding='CP949' 한글 사용 하기 위한 것
print(weather)
print(weather.head())
print(type(weather))
print("기상 데이터의 전반적인 정보 : ",weather.describe())
print('평균 : {}'.format(weather.mean()))
print('표준 편차 : {}'.format(weather.std()))
#print('weather 데이터의 shape : ', weather.shape)

print("최대 풍속 : ",weather['최대풍속'].max())
print(f"평균 풍속 : {weather['평균풍속'].max()}")
print(weather.count())
missing_mean_wind = weather[weather['평균풍속'].isna()]
print(missing_mean_wind)
print(missing_mean_wind.count())
missing_max_wind = weather[weather['최대풍속'].isna()]
print(missing_max_wind)
print(missing_max_wind.count())

new_weather = weather.dropna(axis=0, how='any',inplace=False)
print(new_weather.describe())