
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.suject = subject

t = Teacher("Rayyan", "Programming")
print(t.name)
print(t.suject)

       
        
        
