a,b=input().split()
a=int(a)
b=int(b)
if b>=45:
    b=b-45
elif b<45:
    a=a-1
    if a<0:
        a=23
    b=60+b-45
print(a,b)