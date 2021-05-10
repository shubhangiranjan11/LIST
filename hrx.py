x=int(input("any number"))
y=int(input("any number"))
while y!=0:
    x,y=y,x%y
print(x)