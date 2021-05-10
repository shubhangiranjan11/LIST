list=[20,90,89,76,45,55,34,23,12]
sec=0
max=0
i=0
index=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    i=i+1
while index<len(list):
    if sec<list[index]<max:
        sec=list[index]
    index=index+1
print(sec)

