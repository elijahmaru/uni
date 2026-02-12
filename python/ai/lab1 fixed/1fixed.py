"""
Описание: Программа принимает список всех оценок и последовательно анализирует его элементы. В процессе работы определяется максимальная и минимальная оценка, количество оценок и их сумма. После заверщения цикла количество оценок делится на их сумму чтобы посчитать среднюю оценку. Результатом работы программы является максимальная, минимальная и средняя оценка и количетво
"""


def findMaxMinAvg(allGrades):
    """
    Computes lowest, highest, average grade and their amount

    Parameters:
        allGrades (list of int): List of all grades

    Returns:
        tuple: maximum, lowest, average grade and their amount
    """
    count = 0
    sumOfGrades = 0
    highiestGrade = allGrades[0]
    lowestGrade = allGrades[0]

    for grade in allGrades:
        # updates count
        count = count + 1
        sumOfGrades = sumOfGrades + grade
        # updates maximum grade if current grade is higher and lowest grade if lower
        if grade > highiestGrade:
            highiestGrade = grade
        if grade < lowestGrade:
            lowestGrade = grade
    # computes average grade
    average = sumOfGrades / count
    return highiestGrade, lowestGrade, average, count


grades = [85, 92, 78, 96, 88, 75, 90, 82, 95, 87]
maxGrade, minGrade, averageGrade, amountOfGrades = findMaxMinAvg(grades)
print(f"Count: {amountOfGrades}")
print(f"Average: {averageGrade:.2f}")
print(f"Highest: {maxGrade}")
print(f"Lowest: {minGrade}")
