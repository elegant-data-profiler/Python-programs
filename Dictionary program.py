my_friend={"name":"padma","age":21,"job":"software"}
my_self={"myself":"kavitha","age":21,"job":"still reading"}
del my_friend["age"]
for i,j in zip(my_friend,my_self):
    print(i+":",my_friend[i])
    print(j+":",my_self[j])
print("kavithavarsha and padma both are good friends")    