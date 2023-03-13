class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age}, {self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age}, {self.gender}, {self.record_book}'

class GroupOverflowError(Exception):
    pass

class Group:

    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupOverflowError(f"Group {self.number} is full (max {self.MAX_STUDENTS} students)")
        self.group.add(student)

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

for i in range(10):
    try:
        st = Student('Male', 20 + i, f'Name{i}', f'Surname{i}', f'AN{i}')
        gr.add_student(st)
    except GroupOverflowError as e:
        print(f"Error: {e}")
        break
print(gr)