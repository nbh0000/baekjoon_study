sentence = """
이렇게하면
문단처럼 엔터까지
가능
"""
print(sentence)


#문자열은 배열처럼 출력 가능, 공백은 생략
#몇 번째 부터 ~ 변수[x:y] : x부터 y-1번째까지
#예시 971208-1934567
mynum ="971208-1934567"
print("몇년생 mynum[0:2] : ",mynum[0:2])
print("몇월몇일 mynum[3:5] : ",mynum[2:6])
print("남?녀? : print[7:9] : ", mynum[7:9])
print("주민번호 앞자리 mynum[:6] :", mynum[:6])
print("주민번호 뒷자리 mynum[7:] :", mynum[7:])

# upper, lower : 대문자로, 소문자로 만들기
py = "AbcDefG"
print("py.upper : ",py.upper())
print("py.lower : ",py.lower())
# len : 문자열길이 출력
print("len(py) : ",len(py))

# replace : 단어바꾸기
print("py.replace(\"Abc\",\"Scv\") : ",py.replace("Abc","Scv"))

# index : 어떤 문자가 어느위치에 있는지, 대소문자 구문해줘야함
print("py.index(\"A\") :",py.index("A"))
print("py.index(\"b\") :",py.index("b"))
print("py.index(\"c\") :",py.index("c"))
print("py.index(\"D\") :",py.index("D"))

# find : index와 같음
print("py.find(\"A\") : ", py.find("A"))
print("py.find(\"b\") : ", py.find("b"))

# count : 갯수출력
print("py.count(\"A\")",py.count("A"))
