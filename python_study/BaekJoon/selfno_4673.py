selfno =list(range(1,10000))

for i in range(1,10000):
    L =len(str(i))
    if(L==1):
        A=i+i
        selfno.remove(A)
    elif(L==2):
        A=i%10
        B=int(i/10)
        answer=i+A+B
        selfno.remove(answer)
    elif(L==3):
        A=i//100
        B=(i%100)//10
        C=i%10
        answer = i+A+B+C
        if(answer not in selfno):
            ()
        else:
              selfno.remove(answer)
    elif(L==4):
        A=i//1000
        B=int((i/100)%10)
        C=int((i/10)%10)
        D=i%10
        answer = i+A+B+C+D
        if(answer not in selfno):
            ()
        else:
              selfno.remove(answer)
f =len(selfno)
for i in range(f):
    print(str(selfno[i]).rstrip(''))
print("aa")
