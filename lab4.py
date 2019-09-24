class University:
	def __init__(self):
		self.id=None
		self.age=None
		self.marks=None
	def validate_marks(self):
		if self.marks>=0 and self.marks<=100:
			print("valid marks")
			return True
		return False
	def validate_age(self):
		if self.age>=20:
			print("valid age")
			return True
		return False
	def check_qualification(self):
		if self.marks>=65:
			return True
		return False
	def setter(self):
		self.id=input("Enter id:")
		self.age=int(input("Enter Age:"))
		self.marks=float(input("Enter marks:"))
	def getter(self):
		print("ID :",self.id)
		print("AGE :",self.age)
		print("MARKS :",self.marks)
u=University()
u.setter()
u.getter()
if u.check_qualification():
	print("Student Qualify for Admission")
else:
	print("Student not Qualify for Admission")
