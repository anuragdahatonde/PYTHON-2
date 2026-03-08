class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def display(self):
        print(self.name,self.age)

class student(Person):
    def __init__(self,name,age,marks):
        Person.__init__(self,name,age)
        self.marks = marks

    def stud(self):
        print(" I am a student")

stud1 = student("ANURAG" , 18, 69)
stud1. stud()
stud1.marks = 65
stud1.name = "anu"  
stud1.display()
      
