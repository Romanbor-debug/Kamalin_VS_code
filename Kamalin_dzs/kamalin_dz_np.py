import numpy as np

#task 1

# a = np.array([5, 2, 8, 1, 9, 3])

# print(a.ndim)
# print(a.shape)
# print(a.dtype)
# print(a.size)

#task 2

# a = np.arange(15, 31)
# b = np.linspace(0, 1, 10)

# print(a, b)

#task 3

# a = np.zeros((4, 5), dtype=int)
# b = np.ones((3, 3), dtype=int)
# c = np.random.randint(10, 50, (2, 6))

# print(a)
# print(b)
# print(c)

#task 4

# a = np.arange(0, 21, dtype=int)

# print(a[:5])
# print(a[:-5:-1])
# print(a[::2])
# print(a[::-1])

#task 5

# a = np.arange(25).reshape(5, 5)
# print(a[:,1])
# print(a[-2:])
# print(a[0:2, -2:])
# print(a[4][0])

#task 6

# a = np.array([4, 9, 16, 25])
# b = np.array([2, 3, 4, 5])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(np.sqrt(a))
# print(np.sqrt(b))
# print(np.power(a, b))

#task 7

# data = np.random.randint(1, 100, 20)

# print(data)
# print(sum(data))
# print(sum(data) / len(data))
# print(min(data))
# print(max(data))
# print(np.argmax(data))

#task 8

# a = np.array([12, 45, 2, 78, 31, 5, 96, 14, 67, 23])

# mask = a > 30 #фильтр (будет True при елементе больше 30 и False есле меньше)
# print(a[mask]) #фильтруем

# mask2 = a % 2 == False #True при чётном числе
# print(mask2)

# mask3 = [-1 if i < 10 else int(i) for i in a]

# print(mask3)

#task 9

# a = np.arange(1, 13)

# print(a.reshape(3, 4))
# print(a.reshape(2, 3, 2))
# print(a.reshape(3, 4).ravel())

#task 10

scores = np.array([75, 42, 98, 55, 67, 89, 91, 78, 63, 84, 51, 72, 95, 81, 36, 47, 100, 69, 88, 57])

print(sum(scores) / len(scores))
print(max(scores))
print(min(scores))

mask = scores >= 85

print(sum(mask))

mask2 = scores < 60

print(sum(mask2))

mask3 = [int(i) + 5 if int(i) + 5 <= 100 else 100 for i in scores]

print(mask3)