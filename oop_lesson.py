class Student:
    def __init__(self, name, year):
        self.grades = []
        self.name = name
        self.year = year

    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.grades.append(grade)

    def get_average(self):
        total_score = 0
        for i in self.grades:
            total_score += i.score
        return total_score / len(self.grades)


class Grade:
    minimum_passing = 65

    def __init__(self, score) -> None:
        self.score = score

    def is_passing(self):
        return self.score > Grade.minimum_passing


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))

for grade in pieter.grades:
    print(grade.score)
    print(grade.is_passing())

print(pieter.grades[0].score)
print(pieter.grades[0].is_passing())
print(pieter.get_average())
