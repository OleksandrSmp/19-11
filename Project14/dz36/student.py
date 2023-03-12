from Project14.dz36.human import Human

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age}, {self.gender}, {self.record_book}'

    def __hash__(self):
        return hash(self.record_book)

    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book