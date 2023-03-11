class Counter:
    def __init__(self, current=0, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value
    def set_current(self, start):
        self.current = start
    def set_max(self, max_val):
        self.max_value = max_val
    def set_min(self, min_val):
        self.min_value = min_val
    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Достигнут максимум")
        self.current += 1
    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Достигнут минимум")
        self.current -= 1
    def get_current(self):
        return self.current
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10
try:
    counter.step_up()  # ValueError
except ValueError as e:
    assert str(e) == "Достигнут максимум"
assert counter.get_current() == 10
counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7
try:
    counter.step_down()  # ValueError
except ValueError as e:
    assert str(e) == "Достигнут минимум"
assert counter.get_current() == 7