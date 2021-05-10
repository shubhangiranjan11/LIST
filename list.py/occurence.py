char_list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
a,n,t,u,g,x=0,0,0,0,0,0
i=0
while i<len(char_list):
    if char_list[i]=="a":
        a+=1
    elif char_list[i]=="n":
        n+=1
    elif char_list[i]=="t":
        t+=1
    elif char_list[i]=="u":
        u+=1
    elif char_list[i]=="g":
        g+=1
    elif char_list[i]=="x":
        x+=1
    i=i+1
print(a)
print(n)
print(t)
print(u)
print(g)
print(x)
