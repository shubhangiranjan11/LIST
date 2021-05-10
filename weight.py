num=int(input("any number"))
m=num
r=0
while num>0:
    c=num%10
    r=r*10+c
    num=num//10
if r==m:
    print("palindrome number")
else:
    print("is not palindrome number")