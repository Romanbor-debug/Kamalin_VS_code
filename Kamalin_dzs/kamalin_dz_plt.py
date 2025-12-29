import matplotlib.pyplot as plt
import numpy as np
from random import randint


#task 1
# x = [i for i in np.linspace(-5, 5, 10000)]
# y = [i**2 for i in x]

# plt.axhline(color="black")
# plt.axvline(color="black")
# plt.grid(True)
# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("График функции y = x^2")
# plt.show()

#task 2

# x = [randint(-1000, 1000) for i in range(100)]
# y = [randint(-1000, 1000) for i in range(100)]


# plt.grid(True)
# plt.axhline(color="black")
# plt.axvline(color="black")
# plt.scatter(x, y, marker="o", alpha=0.5)
# plt.show()

#task 3

# days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
# sales = [120, 135, 140, 155, 160, 185, 90]
# colors = ['skyblue', 'lightgreen', 'salmon', 'gold', 'plum', 'orange', 'lightgray']

# plt.grid(True)
# plt.axhline(color="black")
# plt.axvline(color="black")
# plt.bar(days, sales, color=colors)
# plt.show()

#task 4

# categories = ['Аренда', 'Еда', 'Транспорт', 'Развлечения', 'Сбережения']
# expenses = [40000, 20000, 8000, 12000, 10000]
# explode = (0.1, 0, 0, 0, 0)


# plt.pie(expenses, labels=categories, explode=explode)
# plt.show()

#task 5

fig, axis = plt.subplots(2, 2, figsize=(7, 7))

x1 = [i for i in np.linspace(-10, 10, 1000)]
x2 = [i for i in np.linspace(-10, 10, 10)]
y1 = [np.sin(i) for i in x1]
y2 = [randint(0, 100) for i in x2]

x3 = [1, 2, 3, 4, 5, 6, 7, 8]
y3 = [20, 40, 39, 16, 31, 100, 57, 45]

for i in range(2):
    for j in range(2):
        axis[i][j].axhline(color="black")
        axis[i][j].axvline(color="black")
        axis[i][j].grid(True)

axis[0][0].plot(x1, y1)
axis[0][1].bar(x2, y2)
axis[1][0].scatter(x2, y2)
axis[1][1].pie(y3, labels=x3)
plt.show()