n=[10,11,12,13,14,15]
num=30
i=0
c=[]
while i<len(n)-1:
    a=[]
    j=i+1
    while j<len(n):
        if n[i]+n[j]==num and n[i]<n[j]:
            a.append(n[i])
            a.append(n[j])
            c.append(a)
        j=j+1
    i=i+1
print(a)