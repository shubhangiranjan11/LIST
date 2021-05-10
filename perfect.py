i=1
sum=0
n=int(input("any number"))
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print("is a perfect number")
else:
    print("is not a perfect number")
