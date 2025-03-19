import seaborn as sns
import pandas as pd
titanic = sns.load_dataset(name='titanic')
print(titanic)
titanic.to_csv('titanic.csv',index = False)
print(titanic.isnull().sum())   # missing value 확인

titanic['age'] = titanic['age'].fillna(titanic['age'].median())
print(titanic['age'].isnull().sum())
print(titanic['embarked'].value_counts())
titanic['embarked'] = titanic['embarked'].fillna('S')
print(titanic['embarked'].isnull().sum())
print(titanic['embark_town'].value_counts())
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
print(titanic['embark_town'].isnull().sum())
print(titanic['deck'].value_counts())
titanic['deck'] = titanic['deck'].fillna('C')
print(titanic['deck'].isnull().sum())

print(titanic.info)
print(titanic.describe())

print(titanic['survived'].value_counts())

import  matplotlib.pyplot as plt
(fig, ax) = plt.subplots(1,2)
(titanic['survived'][titanic['sex']== 'male'].value_counts()
 .plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[0], shadow=True))
(titanic['survived'][titanic['sex']== 'female'].value_counts()
 .plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[1], shadow=True))
ax[0].set_title('Survived(Male)')
ax[1].set_title('Survived(Female)')
plt.show()