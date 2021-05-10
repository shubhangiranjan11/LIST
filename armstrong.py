num=int(input("any number"))
tem=num
count=len(str(num))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem**count
    num=num//10
if sum==tem:
    print("armstrong number")
else:
    print("not armstrong number")
    