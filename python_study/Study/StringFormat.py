print("a"+"b") #합쳐짐
print("a","b") #그냥 두개 출력됨

#문자열을 합치는 다른방법
# (1) %d %s %c 등 이용
num =20
str ="aa"
ch = "a"
print(" 숫자 : %d " %num)
print(" 문자열 %s" %str)
print(" 문자 %c " %ch)
print("두개이상출력 문자1 : %s 문자2 : %c" %(str,ch))

#중괄호, 포맷이용
print("포맷, 중괄호사용 숫자 : {}".format(num))
print("두개이상 숫자 : {}, 문자열 :{}".format(num,str))
#중괄호안에 숫자넣으면 그 순번에 맞게 출력

