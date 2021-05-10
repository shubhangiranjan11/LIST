elements=[23,14,56,12,18,19,9,15,25,31,42,43]
i=0
sum_odd_no=0
sum_even_no=0
while i<len(elements):
    if elements[i]%2==0:
        sum_odd_no+=elements[i]
    else:
        sum_even_no+=elements[i]
    i=i+1
print(sum_odd_no)
print(sum_even_no)