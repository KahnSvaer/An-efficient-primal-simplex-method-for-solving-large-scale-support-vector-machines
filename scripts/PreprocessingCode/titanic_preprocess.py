import pandas as pd

data = pd.read_csv("../../data/raw/Titanic-Dataset.csv")
data['Title'] = data['Name'].apply(lambda name: name.split(',')[1].split('.')[0].strip())
data['Is_Young'] = data['Title'].apply(lambda title: 1 if title in ['Master', 'Miss'] else 0)
data = data.drop(columns=['PassengerId', 'Name', 'Ticket','Fare', 'Cabin', 'Title'])
data = data.dropna()
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'],dtype=int)
data.to_csv('../../data/processed/titanic_dataset.csv', sep=',', index=False, encoding='utf-8')
