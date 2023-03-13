from Project14.dz36.human import Human

class Student(Human):

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (self.gender == other.gender
                and self.age == other.age
                and self.first_name == other.first_name
                and self.last_name == other.last_name
                and self.record_book == other.record_book)

