name=["n","i","t","i","n"]
index=-1
a=[]
while index>=(-len(name)):
    a.append(name[index])
    index=index-1
if name==a:
    print("palindrome number")
else:
    print("not palindrome number")