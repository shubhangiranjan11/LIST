elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even=0
odd=0
sum_even=0
sum_odd=0
while i<len(elements):
    if elements[i]%2==0:
        even+=1
        sum_even+=elements[i]
    else:
        odd+=1
        sum_odd+=elements[i]
    i=i+1
print("average even=",even/sum_even)
print("average odd=",odd/sum_odd)
