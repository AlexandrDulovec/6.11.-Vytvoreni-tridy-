class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def display_info(self):
        print(f"Student: {self.name} {self.surname}")
        print("Známky:", ", ".join(map(str, self.grades)))

student1 = Student("Alexandr", "Dulovec", [1, 1, 1])
student1.display_info()
