num=[1,2,3,4,5,6,7,8]
num1=[1,3,8,6,7,8]
a=[]
index=0
while index<len(num):
    if num[index]not in num1:
        a.append(num[index])
    index=index+1
print(a)

