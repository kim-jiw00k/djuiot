# LinearRegression = 선형 회귀
from sklearn.linear_model import LinearRegression

regression = LinearRegression() # 생성자
x = [[174], [152], [138], [128], [186]]
y = [71, 55, 46, 38, 88]
regression.fit(X=x, y=y)
print(regression.coef_)     # weight -> 기울기
print(regression.intercept_)# bias -> y 절편
import matplotlib.pyplot as plt
plt.scatter(x,y, color="red")
y_predict = regression.predict(X=x)
plt.plot(x, y_predict, 'b-')
jihyun_weight = regression.predict(X=[[165]])
plt.plot(165, jihyun_weight, 'g*')
plt.show()