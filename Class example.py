class food:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print("name and age")
class tea:
	def __init__(self,taste,type):
		self.taste=taste
		self.type=type
		print("tea so hot")
f=food("kavitha",21)
print(f.name)
print(f.age)
t=tea("nice","hot")
print(t.taste)
print(t.type)