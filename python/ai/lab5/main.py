import numpy as np

# task 1
data = np.random.randint(0, 100, size=10)
print(f"массив: {data}")
rank = np.floor_divide(data, 10)
print(f"ранги : {rank}")

# task 2
data = np.random.randint(40, 100, size=(100, 6))
print(f"исходные оценки: {data.shape}")
avgOfStudent = data.mean(axis=1, keepdims=True)
print(f"среднея оценка студента: {avgOfStudent.shape}")
avgOfDiscipline = data.mean(axis=0, keepdims=True)
print(f"среднея оценка дисциплины: {avgOfStudent.shape}")
goodStudents = np.greater(avgOfStudent, 85)
badStudents = np.less(avgOfStudent, 60)
bestStudent = avgOfStudent.argmax()
worstStudent = avgOfStudent.argmin()
hardestDisciplins = avgOfDiscipline.argsort()[:3]
rankings = np.sort(avgOfStudent)

# task 3
transactions = np.random.randint(-100, 500, size=10000)
balanceHistory = transactions.cumsum()
minBalance = balanceHistory.min()
maxBalance = balanceHistory.max()
criticalBalance = np.less(balanceHistory, 0)

