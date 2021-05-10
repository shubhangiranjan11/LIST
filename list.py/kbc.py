questions_list=["1.how many continents are there?","2.what is capital of india?","3.ng m kon sa course hota hai"]
options_list=[["1.four","2.nine","3.seven","4.eight"],["1.chandigarh","2.bhopal","3.chennai","4.delhi"],["1.software","2.conselling","3.tourism","4.agriculture"]]
solutions_list=[3,4,1]
lifeline_key=[["1.four","3.seven"],["1.chandigarh","4.delhi"],["1.software","4.agricultur"]]
print("there is one lifeline key if you want to use you can use it by entering 5050")
i=0
c=0
while i<len(questions_list):
    print(questions_list[i])
    j=0
    while j<len(options_list[i]):
        print(options_list[i][j])
        j+=1
    user=int(input("any number"))
    if user==solutions_list[i]:
        print("congress")
    elif (user==5050):
        if c==0:
            print(lifeline_key[i])
            c+=1
            user1=int(input("any number"))
            if user1==solutions_list[i]:
                print("congress")
            else:
                print("sadly you are wrong") 
        else:
            print("you already used lifeline key")
            user2=int(input("any number")) 
            if user2==solutions_list[i]:
                print("you are correct")
            else:
                print("you are wrong")
    else:
        print("oops!you guess is wrong")
        print("qiute")
    i=i+1