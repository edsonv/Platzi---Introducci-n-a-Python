class LivingBeign:
    def __init__(self, name):
        self.name = name


class Person(LivingBeign):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Mi student Id is: {self.student_id}")


student = Student("John", 20, "S12345")
student.introduce()
