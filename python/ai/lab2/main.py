def readFile(filePath):
    try:
        file = open(filePath)
    except Exception as e:
        raise e
    return file


def fileToListOfLines(filePath):
    file = readFile(filePath)
    lines = []
    for line in file:
        lines.append(line)
    return lines


listOfEmployees = []
fileName = "employees.csv"
file, err = fileToListOfLines(fileName)
categoryNames = file.pop(0).replace("\n", "").split(",")
for line in file:
    line = line.replace("\n", "")
    valuesSeparated = line.split(",")
    listOfEmployees.append(dict(zip(categoryNames, valuesSeparated)))
    """
    listOfEmployees.append({category: None for category in categoryNames})
    for category in categoryNames:
        listOfEmployees[-1][category] = valuesSeparated[categoryNames.index(
            category)]
    """

listByDepartment = {}
for employee in listOfEmployees:
    if employee["department"] in listByDepartment:
        listByDepartment[employee["department"]].append(
            {key: value for key, value in employee.items() if key != "department"}
        )
    else:
        listByDepartment[employee["department"]] = [
            {key: value for key, value in employee.items() if key != "department"}
        ]
print(listByDepartment["HR"])
"""
Используется словарь так как он хранит данные по из хэшу, что позволяет быстрее и легче обрщаться к данным 
"""
