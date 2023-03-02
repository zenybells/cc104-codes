class Employee:
    newId = 1

    def __init__(self):
        self.id = Employee.newId
        Employee.newId += 1

    def say_id(self):
        return f"My id is {self.id}"


e1 = Employee()
e2 = Employee()
print(e1.say_id())
print(e2.say_id())
