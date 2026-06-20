class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"안녕하세요. {self.name}입니다.")

student = Student("Hyojoon")
student.introduce()
