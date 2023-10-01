class Student:
  def __init__(self, name, student_id, age, gender):
    self.name = name
    self.student_id = student_id
    self.age = age
    self.gender = gender
    self.grade = 0
  def set_grade(self, grade):
    self.grade = grade
  def get_grade(self):
    return self.grade
  def display_student_info(self):
    print("Name:", self.name, "\nStudent_ID:", self.student_id, "\nAge:", self.age, "\nGender:", self.gender, "\nGrade:", self.grade, '\n')
