class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"Roll: {self.roll}, Name: {self.name}, Marks: {self.marks}"


n = int(input("Enter number of students: "))

students = []   # list of objects

for i in range(n):
    print(f"\nEnter details of student {i+1}:")
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))

    obj = Student(roll, name, marks)   # create object
    students.append(obj)               # store object in list


print("\n----- Student Details -----")
for s in students:
    print(s)
