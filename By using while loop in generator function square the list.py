def squr(num):
	for i in num:
		yield(i*i)
list=squr([1,2,3])
for i in list:
	print(i)