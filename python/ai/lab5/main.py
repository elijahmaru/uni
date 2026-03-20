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
worstStudent = avgOfStudent.argmin()[0]
hardestDisciplins = avgOfDiscipline.argsort()[:3]
rankings = np.argsort(avgOfStudent)

# task 3
transactions = np.random.randint(-100, 500, size=10000)
balanceHistory = transactions.cumsum()
minBalance = balanceHistory.min()
maxBalance = balanceHistory.max()
criticalBalance = np.less(balanceHistory, 0)
growth = np.diff(balanceHistory) > 0
growth = np.concatenate(([False], growth, [False]))
borders = np.diff(growth.astype(int))
starts = np.where(borders == 1)[0]
ends = np.where(borders == -1)[0]
lengths = ends - starts
indexOfLongest = lengths.argmax()
startIndex = starts[indexOfLongest]
endIndex = ends[indexOfLongest]
indexOfAnomalyies = np.where(
    transactions.__abs__() > balanceHistory.std() * 3)[0]

# task 4
signal = np.random.randint(0, 10, size=50000)
patterns = {}
windows = np.lib.stride_tricks.sliding_window_view(signal, 5)
patterns, counts = np.unique(windows, axis=0, return_counts=True)

# task 5
matrix = np.random.randint(0, 2, size=(200, 50))
itemPopularity = matrix.sum(axis=0)
topItems = itemPopularity.argsort()[::-1]


def similarity(first: np.ndarray, second: np.ndarray) -> np.float16:
    return np.linalg.norm(first - second)


similarityMatrix = np.zeros((200, 200))
similarityMatrix = np.linalg.norm(
    matrix[:, None, :] - matrix[None, :, :], axis=2)
recommendationsToUsers = np.zeros(200)
for targetUser in range(200):
    similarUsers = similarityMatrix[targetUser].argsort()
    similarUsers = similarUsers[similarUsers != targetUser][:5]
    similarItems = matrix[similarUsers].sum(axis=0)
    userItems = matrix[targetUser]
    recommendations = similarItems * (1 - userItems)
    recommendations = np.argsort(recommendations)[::-1][:5]
    recommendationsToUsers[targetUser](recommendations)
