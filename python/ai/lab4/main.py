import time
import numpy as np

# task 1
data = np.random.rand(24 * 60, 12)
print(f"Исходная форма: {data.shape}")
dataReshaped = data.reshape(24, 60, 12)
if data[0][0] == dataReshaped[0][0][0] and data[60][0] == dataReshaped[1][0][0]:
    data = dataReshaped
else:
    raise TypeError("Reshape wasn't done properly")
print(f"Изменённая форма: {data.shape}")
avgPerHour = data.mean(axis=(1, 2))
avgPerSensor = data.mean(axis=(0, 1))
avgPerHourAndSensor = data.mean(axis=1)
dataNotLinear = data / (1 + np.abs(data))
if data.shape == dataNotLinear.shape:
    dataDelta = np.abs(data - dataNotLinear)
    maxChange = dataDelta.max()
    data = dataNotLinear
else:
    raise TypeError(
        "Wrong shape of the array after application of the formula")
print("Максимальное изменение: ", maxChange)

# task 2
np.random.seed(0)
X = np.random.rand(500, 5)
centerOfMass = X.mean(axis=0)
xCentered = X - centerOfMass
if np.allclose(xCentered.mean(axis=0), 0):
    X = xCentered
    print("Массив центрирован")
else:
    raise ValueError("Array is not centered properly")
startTime = time.perf_counter()
diff = X[:, None, :] - X[None, :, :]
d1 = np.sqrt(np.sum((diff**2), axis=2))
endTime = time.perf_counter()
print(d1)
timeForD1 = endTime - startTime
startTime = time.perf_counter()
norms = np.sum(X**2, axis=1)
d2 = np.sqrt(np.maximum(norms[:, None] + norms[None, :] - 2 * X @ X.T, 0))
endTime = time.perf_counter()
timeForD2 = endTime - startTime
print(f"Время для первого: {timeForD1}\nВремя для второго: {timeForD2}")
i, j = np.unravel_index(np.argmin(d1 + np.eye(len(d1)) * np.inf), d1.shape)
print(f"Индексы ближайших к друг другу:{i}, {j}")

# task 3
X = np.random.rand(1000, 10)
print(f"Исходная форма: {X.shape}")
euclideanNorm = np.sqrt(np.sum(np.square(X), axis=1))
print(f"{euclideanNorm.shape}")
X = X / euclideanNorm[:, None]
euclideanNorm = np.linalg.norm(X, axis=1)
print(f"Проверка нормалей{np.allclose(euclideanNorm, 1)}")

print()

X = np.random.rand(500, 20)
startShape = X.shape
avgPerRow = X.mean(axis=1)
print(f"Форма среднего по строке{avgPerRow.shape}")
avgPerRow = avgPerRow[:, None]
avgPerCol = X.mean(axis=0)
print(f"Форма среднего по столбцу{avgPerCol.shape}")
avgPerCol = avgPerCol[None, :]
boolMask = (X > avgPerRow) & (X < avgPerCol)
X[boolMask] = 0
endShape = X.shape
replacementCount = np.sum(boolMask)
print(f"Элементов изменено: {replacementCount}")
print(f"Провекрка неизменности формы :{startShape == endShape}")
