def string(n):
    for i in n:
        if i%2==0:
            print('even')
        else:
            print('odd')
n=(1,2,3,4)
print(string(n))