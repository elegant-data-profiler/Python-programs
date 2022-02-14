class family:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def my_family(f):
		print("my father name is"+f.name+" "+f.age)
class father(family):
	def __init__(self,name,age,work):
		super() .__init__(name,age)
		self.work=work
class mother(father):
	def	__init__(self,name,age,work,year):
		super().__init__(name,age,work)
		self.year=year
	def my_mother(s):
		print("my mother name is","",s.name,"b","age ",s.age,"",s.work)
m=mother("chennamma",40,"sales fruits",2022)
m.my_mother()

