import time
import numpy as np

# task 1
data = np.random.rand(24 * 60, 12)
dataReshaped = data.reshape(24, 60, 12)
print(data.shape)
if data[0][0] == dataReshaped[0][0][0] and data[60][0] == dataReshaped[1][0][0]:
    data = dataReshaped
else:
    raise TypeError("Reshape wasn't done properly")
print(data.shape)
avgPerHour = data.mean(axis=(1, 2))
avgPerSensor = data.mean(axis=(0, 1))
avgPerHourAndSensor = data.mean(axis=1)
dataNotLinear = data / (1 + abs(data))
if data.shape == dataNotLinear.shape:
    dataDelta = abs(data - dataNotLinear)
    maxChange = dataDelta.max()
    data = dataNotLinear
else:
    raise TypeError("Wrong shape of the array after application of the formula")
print("Максимальное изменение: ", maxChange)

# task 2
np.random.seed(0)
X = np.random.rand(500, 5)
centerOfMass = X.mean(axis=0)
xCenterd = X - centerOfMass
if np.allclose(xCenterd.mean(axis=0), 0):
    print("Массив центрирован")
else:
    raise ValueError("Array is not centered properly")
startTime = time.perf_counter()
diff = X[:, None, :] - X[None, :, :]
d1 = np.sqrt(np.sum((diff * 2), axis=2))
endTime = time.perf_counter()
print(d1.shape)
timeForD1 = endTime - startTime
startTime = time.perf_counter()
norms = np.sum(X**2, axis=1)
d2 = np.sqrt(norms[:, None] + norms[None, :] - 2 * X @ X.T)
endTime = time.perf_counter()
timeForD2 = endTime - startTime
print(f"Время для первого: {timeForD1}\nВремя для второго: {timeForD2}")
indexOfClothestPoint = np.argmin(d1)

# task 3
