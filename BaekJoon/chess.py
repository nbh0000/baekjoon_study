chs = [1,1,2,2,2,8]
chs1 =[]
chsRs =[]
a=input().split()
for i in range(0,6):
    chs1.append(int(a[i]))
    chsRs.append(chs[i]-chs1[i])
    print(chsRs[i])

