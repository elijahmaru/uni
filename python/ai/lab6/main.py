import pandas as pd
import numpy as np

# task 1
initialReport = {}
dataSet = pd.read_csv("dataSet.csv")
print("File loaded")
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
amountOfNaN = dataSet.isna().sum().sum()
amountOfDublicates = dataSet.duplicated(keep=False).sum()
amountOfUnique = dataSet.nunique()
top5 = dataSet.select_dtypes(include=["string", "object"]).value_counts().head()
print("INITIAL REPORT")
initialReport.update({"missing": amountOfNaN, "duplicates": amountOfDublicates})
print(initialReport)

# task 2
dataSetClean = dataSet.copy()
dataSetClean.fillna(dataSetClean.median(numeric_only=True), inplace=True)
afterNumFill = amountOfNaN - dataSetClean.isna().sum().sum()
amountOfNaN = dataSetClean.isna().sum().sum()
datesCol = ["time", "year", "month", "day_of_year", "hour"]
dataSetClean["time"].replace("", np.nan, inplace=True)
dataSetClean.dropna(subset=["time"], inplace=True)
afterTimeDelete = amountOfNaN - dataSetClean.isna().sum().sum()
amountOfNaN = dataSetClean.isna().sum().sum()
dataSetClean.fillna(
    dataSetClean.mode().iloc[0], inplace=True
)  # заполнеят все пустые места модой
afterStringFill = amountOfNaN - dataSetClean.isna().sum().sum()
amountOfNaN = dataSetClean.isna().sum().sum()
dataSetClean.drop_duplicates(keep="first")
dataSetClean.reset_index(drop=True, inplace=True)
print("INFO:\nDataSet before cleaning:\n", dataSet.info())
print("DataSet after cleaning:\n", dataSetClean.info())

# task 3
