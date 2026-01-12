import pandas as pd

df = pd.read_csv('task/stackoverflow_qa.csv')
df['creationdate'] = pd.to_datetime(df['creationdate'])


df[df['creationdate'].dt.year < 2014]

df[df['score'] > 50]

df[(df['score'] >= 50) & (df['score'] <= 100)]

df[df['ans_name'] == 'Scott Boston']

users = ['Scott Boston','unutbu','Mike Pennington','unutbu','Demitri']
df[df['ans_name'].isin(users)]

mask = (df['creationdate'] >= '2014-03-01') & \
       (df['creationdate'] <= '2014-10-31') & \
       (df['ans_name'] == 'Unutbu') & \
       (df['score'] < 5)

df[mask]

df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]

df[df['ans_name'] != 'Scott Boston']

import pandas as pd
titanic_df = pd.read_csv("task/titanic.csv")

df1 = titanic_df[(titanic_df['Sex'] == 'female') &
                 (titanic_df['Pclass'] == 1) &
                 (titanic_df['Age'].between(20, 30))]

df2 = titanic_df[titanic_df['Fare'] > 100]

df3 = titanic_df[(titanic_df['Survived'] == 1) &
                 (titanic_df['SibSp'] == 0) &
                 (titanic_df['Parch'] == 0)]

df4 = titanic_df[(titanic_df['Embarked'] == 'C') &
                 (titanic_df['Fare'] > 50)]

df5 = titanic_df[(titanic_df['SibSp'] > 0) &
                 (titanic_df['Parch'] > 0)]

df6 = titanic_df[(titanic_df['Age'] <= 15) &
                 (titanic_df['Survived'] == 0)]

df7 = titanic_df[(titanic_df['Cabin'].notnull()) &
                 (titanic_df['Fare'] > 200)]

df8 = titanic_df[titanic_df['PassengerId'] % 2 == 1]

unique_tickets = titanic_df['Ticket'].value_counts()
unique_tickets = unique_tickets[unique_tickets == 1].index

df9 = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]

df10 = titanic_df[(titanic_df['Name'].str.contains('Miss')) &
                  (titanic_df['Sex'] == 'female') &
                  (titanic_df['Pclass'] == 1)]

