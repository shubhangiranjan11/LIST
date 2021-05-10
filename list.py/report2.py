marks=[[78,64,94,86,88],[91,71,98,65,76],[45,48,28,52,79]]
i=0
s=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        s=s+marks[i][j]
        j=j+1
    i=i+1
print("average",s/i)