class buckets:
    def __init__(self, first_bucket: int, second_bucket: int):
        self.setBuckets(first_bucket, second_bucket)

    def setBuckets(self, first, second):
        first_valid = 0 <= first <= 4
        second_valid = 0 <= second <= 7
        if not first_valid and not second_valid:
            raise ValueError(
                "Both values are out of range: first must be 0–4 and second must be 0–7"
            )
        if not first_valid:
            raise ValueError("first must be between 0 and 4")
        if not second_valid:
            raise ValueError("second must be between 0 and 7")
        self._first = first
        self._second = second

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        # validate together with current second
        self.setBuckets(value, self._second)

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        self.setBuckets(self._first, value)


def fillFirst(state):
    if state._first == 4:
        raise ValueError("First bucket is already full")
    state._first = 4


def fillSecond(state):
    if state._second == 7:
        raise ValueError("Second bucket is already full")
    state._second = 7


def pourOutFirst(state):
    if state._first == 0:
        raise ValueError("First bucket is already empty")
    state.setBuckets(0, state._second)


def pourOutSecond(state):
    if state._second == 0:
        raise ValueError("Second bucket is already empty")
    state.setBuckets(state._first, 0)


def pourFtoS(state):
    if state._second == 7:
        raise ValueError("Second bucket is already full")
    if state._first == 0:
        raise ValueError("First bucket is already empty")
    firstFuture = state._first - (7 - state._second)
    if firstFuture < 0:
        firstFuture = 0
    secondFuture = state._second + state._first
    if secondFuture > 7:
        secondFuture = 7
    state.setBuckets(firstFuture, secondFuture)


def pourStoF(state):
    if state._second == 0:
        raise ValueError("Second bucket is already empty")
    if state._first == 4:
        raise ValueError("First bucket is already full")
    secondFuture = state._second - (4 - state._first)
    if secondFuture < 0:
        secondFuture = 0
    firstFuture = state._first + state._second
    if firstFuture > 4:
        firstFuture = 4
    state.setBuckets(firstFuture, secondFuture)


def printBucket(state: buckets):
    print(f"Первый кувшин: {state.first}, второй кувшин: {state.second}")


def isGoal(state: buckets):
    return state.first == 2 or state.second == 2


# Наполнить второй -> (0, 7)
# Перелить в первый -> (4, 3)
# Вылить первы -> (0, 3)
# Перелить в первый ->(3, 0)
# Наполнить второй ->(3, 7)
# Перелить в первый ->(4, 6)
# Вылить первый ->(0, 6)
# Перелить в первый ->(4, 2)

listOfActions = [fillSecond, pourStoF, pourOutFirst, pourStoF, fillSecond, pourStoF, pourOutFirst, pourStoF]
world = buckets(0, 0)
for action in listOfActions:
    action(world)
    printBucket(world)
    if isGoal(world):
        print("Ответ получен")
