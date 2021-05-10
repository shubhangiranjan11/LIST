i=2
while i<100:
    j=2
    c=0
    while j<i:
        if i%j==0:
            c+=1
        j+=1
    if c==0:
        print(i,"prime number")
    else:
        print(i,"not prime number")
    i+=1

