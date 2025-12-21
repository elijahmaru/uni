class buckets:
    def __init__(self, firstBucket, secondBucket):
        if not 0 <= firstBucket <= 4:
            raise ValueError("First bucket must be between 0 and 4")
        self.first = firstBucket
        if not 0 <= secondBucket <= 7:
            raise ValueError("Second bucket must be between 0 and 7")
        self.second = secondBucket


def isGoal(state: buckets):
    return state.first == 2 or state.second == 2

word = buckets(int(input()), int(input()))
