a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
odd=0
even=0
sum=0
c=0
sum_odd=0
sum_even=0
while i<len(a):
    c+=1
    sum+=a[i]
    if a[i]%2==0:
        even+=1
        sum_even+=a[i]
    else:
        odd+=1
        sum_odd+=1
    i=i+1
print(c)
print(sum)
print(sum/c)
print(odd)
print(even)
print(sum_even)
print(sum_odd)
print(sum_even/even)
print(sum_odd/odd)