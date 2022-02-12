def set(a,b):
    for num in range(a,b+1):
        if num>1:
            for i in range(4,num):
                if num%2==0:
                    break
                else:
                    print(num)
print(set(4,10))       