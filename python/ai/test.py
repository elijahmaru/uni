class buckets:
    def __init__(self, first_bucket: int, second_bucket: int):
        self._set_buckets(first_bucket, second_bucket)

    def _set_buckets(self, first, second):
        first_valid = 0 <= first <= 4
        second_valid = 0 <= second <= 7

        if not first_valid and not second_valid:
            raise ValueError(
                "Both values are out of range: "
                "first must be 0–4 and second must be 0–7"
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
        self._set_buckets(value, self._second)

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        # validate together with current first
        self._set_buckets(self._first, value)

def isGoal(state: buckets):
    return state.first == 2 or state.second == 2


w = buckets(1, 7)
print(w)
w.first = 40
