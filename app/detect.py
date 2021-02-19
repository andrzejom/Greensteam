import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import plot_confusion_matrix

train_dataset = pd.read_csv('train.csv')

key = False
if key:
    colormap = plt.cm.RdBu
    plt.figure(figsize=(14, 12))
    plt.title('Pearson Correlation of Features', y=1.05, size=15)
    sns.heatmap(train_dataset.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
    plt.show()
#Dropping less relevant data
train_dataset_ref = train_dataset.drop(['PassengerId','Cabin'],axis=1)
#print(train_dataset_ref.shape)
#Changing data representation for Sex
train_dataset_ref['Sex']=train_dataset_ref.loc[ train_dataset_ref['Sex'] == 'male', 'Sex'] = 0
train_dataset_ref['Sex']=train_dataset_ref.loc[ train_dataset_ref['Sex'] == 'female', 'Sex'] = 1
train_dataset_ref['Sex']=train_dataset_ref['Sex'] = train_dataset_ref['Sex'].astype(int)
#To simply the data representation mapping age to 3 categories
train_dataset_ref['Age']=train_dataset_ref.loc[ train_dataset_ref['Age'] <= 18, 'Age'] = 0
train_dataset_ref['Age']=train_dataset_ref.loc[(train_dataset_ref['Age'] > 18) & (train_dataset_ref['Age'] <= 54), 'Age'] = 1
train_dataset_ref['Age']=train_dataset_ref.loc[ train_dataset_ref['Age'] > 54, 'Age'] = 2
#To simply the data representation mapping fare to 4 categories
train_dataset_ref['Fare']=train_dataset_ref.loc[ train_dataset_ref['Fare'] <= 10, 'Fare'] = 0
train_dataset_ref['Fare']=train_dataset_ref.loc[(train_dataset_ref['Fare'] > 10) & (train_dataset_ref['Fare'] <= 50), 'Fare'] = 1
train_dataset_ref['Fare']=train_dataset_ref.loc[(train_dataset_ref['Fare'] > 50) & (train_dataset_ref['Fare'] <= 100), 'Fare'] = 2
train_dataset_ref['Fare']=train_dataset_ref.loc[ train_dataset_ref['Fare'] > 100, 'Fare'] = 3
train_dataset_ref['Fare']=train_dataset_ref['Fare'] = train_dataset_ref['Fare'].astype(int)
x = train_dataset_ref[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
y = train_dataset_ref[['Survived']]

regr = linear_model.LinearRegression()
regr.fit(x, y)


def assess_risk(pclass, sex, age, sibsp, parch, fare):
    d = {'Pclass': pclass, 'Sex': sex, 'Age': age, 'SibSp': sibsp, 'Parch': parch, 'Fare': fare}
    df = pd.DataFrame(data=d, index=[0])
    test_data = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
    risk_prediction = regr.predict(test_data)

    return risk_prediction[0][0]
