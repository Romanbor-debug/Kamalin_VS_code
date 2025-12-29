import pandas as pd
import numpy as np

data = pd.read_csv("titanic.csv", index_col=0)

#task 1

# print(data.shape)
# print(data.dtypes)
# print(data.isna().sum().sum())
# print(data[["Age"]].isna().sum())

#task 2

# arr1 = []
# arr2 = []
# names = ["Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch" , "Ticket", "Fare", "Cabin", "Embarked"]

# for i in range(0, len(data.dtypes)):
#     if data.dtypes.iloc[i] == "int64" or data.dtypes.iloc[i] == "float64":
#         arr1.append(names[i])
#     else:
#         arr2.append(names[i])

# print(arr1)
# print(arr2)
# print(data.dtypes)
# print(data[arr1].describe(), end="\n\n")
# print(data[arr2].value_counts(), end="\n\n")

# mask1 = data[["Sex"]] == "male"

# print(mask1.sum())

# mask2 = data[["Pclass"]] == 1

# print(mask2)
# print(mask2.sum())

#task 3

# print(data[["Survived"]].sum())
# print(np.round((data[["Survived"]].sum() / data[["Survived"]].count()) * 100, 2))

# mask1 = data[["Sex"]] == "male"
# mask2 = data[["Sex"]] == "female"

# print(np.round((mask1.sum() / mask1.count()) * 100, 2))
# print(np.round((mask2.sum() / mask2.count()) * 100, 2))

#task 4

# mask1 = data[["Pclass"]] == 1
# a = np.array(data[["Fare"]]) #предпологаю что эта колонна отвечает за цену (другую не нашёл)

# print(mask1)
# print(a[mask1].sum() / mask1.sum())


# print(data[(data.Pclass == 3) & (data.Survived == 1)].count())
# print(data[data.Pclass == 3].count())

# print(data[(data.Pclass == 3) & (data.Survived == 1)].count() / data[data.Pclass == 3].count())

#task 5

# print(data.Age.median())

# print(data.Age.head(20))

# data.Age = data.Age.fillna(data.Age.median())

# print(data.Age.head(20))

#task 6

#Не точное условие (не понял что делать)

#task 7

# print(round(data[data.Survived == 1].Age.describe().iloc[1], 2))
# print(round(data[data.Survived == 0].Age.describe().iloc[1], 2))

#task 8

print(data[(data.Sex == "female") & (data.Survived == 1) & (data.Pclass == 1)].count())
print(data[(data.Age < 18) & (data.SibSp == 0)].count()) #Предположил что SibSp это bool знач показывающее наличиие родственников на корабле

