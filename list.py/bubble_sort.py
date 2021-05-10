a=[6,8,9,7,6,45,9,8]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    i+=1
print(a)


