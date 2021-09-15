from Student import Student

student1 = Student("Jim", "Business", 3.1)
student2 = Student("Pam", "Medical", 3.87)

print(student1.gpa)
print(student2.name, student2.major)

print(student2.on_honor_roll())
print(student1.on_honor_roll())
