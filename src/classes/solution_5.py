class Student:
    def __init__(self, name: str, second_name: str, grade: int) -> None:
        self.name = name
        self.second_name = second_name
        self.grade = grade
        self.marks = dict()

    def add_score(self, subject: str, mark: int) -> None:
        self.marks[subject] = mark


class SchoolJournal:
    def __init__(self) -> None:
        self.pupils = []
        self.average = 0

    def add_student(self, student) -> None:
        self.pupils.append(student)

    def display_all(self) -> None:
        for i in self.pupils:
            print(f"{i.name} {i.second_name}, класс: {i.grade}")
            for j in i.marks:
                print(f"\t{j} : {i.marks[j]}")

    def get_class_average(self, grade: int):
        for i in self.pupils:
            if i.grade != grade:
                continue
            else:
                for j in i.marks:
                    self.average += i.marks[j] / len(i.marks)
        return f"Средний балл в классе {round(self.average / len(self.pupils), 2)}"


school_journal = SchoolJournal()

student_1 = Student("Иван", "Сидоров", 5)
student_1.add_score("Math", 5)
student_1.add_score("History", 4)
student_1.add_score("Biology", 5)
school_journal.add_student(student_1)
school_journal.display_all()
print(school_journal.get_class_average(5))
