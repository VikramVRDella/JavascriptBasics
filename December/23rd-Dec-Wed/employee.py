class Employee:
    def __init__(self, name,role):
        self.name = name
        self.role = role

    def login(self):
        return f"{self.name} is logged in as {self.role}"

class TaskEmployee(Employee):
    pass

class Manager(Employee):
    pass