######숫자함수######
# abs : 절댓값
# pow(x,y) : x의 y제곱
# max(x,y) : x와 y중의 최댓값
# min(x,y) : x와 y중의 최솟값
# round(x) : x의 반올림
# floor(x) : x의 내림
# ceil(x) : x의 올림
# sqrt(x) : x의 제곱근

print('abs(-100):',abs(-100))
print('pow(2,4):',pow(2,4))


#####랜덤함수#####
# from random import *
# random()         : 0.0 ~ 1.0 미만의 임의의 값
# random()*10      : 0.0 ~ 10.0
# int(random()*10) : 0 ~ 10 -> 소수점떨이 
# randrange(x,y)   : x ~ y-1까지 랜덤
# randint(x,y)     : x ~ y까지 랜덤

from random import *
print("random() :", random())
print("int(random())*10:",int(random()*10))

print('오프라인 스터디 모임 날짜는 '+ str(randint(4,28))+'일로 선정되었습니다.')
