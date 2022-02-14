def sample(s):
	dict={1:"kavi",2:"sari"}
	return tuple(dict.fromkeys(s))
x=(1,2,1)
print(sample(x))


