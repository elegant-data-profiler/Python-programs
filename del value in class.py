class student:
	def __init__(self,name,rank):
		self.name=name
		self.rank=rank
		print("my rank")
	def my_func(s):
		print("my"+" "+s.name+" "+"my"+" "+s.rank)
d=student('kavitha',1)
del d.rank
print(d.rank)