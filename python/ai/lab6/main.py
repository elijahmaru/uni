import pandas as pd

initialReport = {}
dataSet = pd.read_csv("dataSet.csv")
print(dataSet)
print("\n" * 5)
print("INFO:")
print(dataSet.info())
print("\n" * 5)
print("DESCRIBE:")
print(dataSet.describe())
print("\n" * 5)
print("SHAPE:")
initialReport["shape"] = dataSet.shape
print(initialReport["shape"])
print("\n" * 5)
print("TYPES:")
initialReport["dtypes"] = dataSet.dtypes
print(initialReport["dtypes"])

amountOfNaN = dataSet.isna().sum()
amountOfDublicates = dataSet.duplicated(keep=False).sum()
amountOfUnique = dataSet.nunique()
top5 = dataSet.select_dtypes(include=["string", "object"]).value_counts().head()
print("INITIAL REPORT")
initialReport.update({"missing": amountOfNaN, "duplicates": amountOfDublicates})
print(initialReport)
