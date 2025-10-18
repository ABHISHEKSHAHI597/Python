class data:
    def __init__(self, name, age, college_year, cgpa):
        self.name = name 
        self.age = age 
        self.college_year = college_year
        self.cgpa = cgpa
# below function is an object function
    def is_a_good_student(self):
        if self.cgpa >= 7.5:
           return True
        else:
           return False