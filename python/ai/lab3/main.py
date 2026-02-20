from random import randint
import feature_processing as fp


def generateRandomArray(
    len: int = 100, startOfRange: int = 0, endOfRange: int = 10
) -> list[int]:
    return [randint(startOfRange, endOfRange) for _ in range(len)]


listA = generateRandomArray()
listB = generateRandomArray()
pipelineForA = [fp.mean, fp.median, fp.variance, fp.std]
pipelineForB = [fp.min_max_scale, fp.log_scale, fp.standardize, fp.remove_outliers]
fp.apply_pipeline(listB, pipelineForB)
for func in pipelineForA:
    print(func(listA))
