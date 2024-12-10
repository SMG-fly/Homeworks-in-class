#다양한 연산자의 활용

#산술 연산자 
'''
 +     -    *   / (사칙연산)
 //(몫만 구함)  %(나머지)    **(거듭제곱)
'''
x = int(input("정수 입력: "))
y1 = x + 10
y2 = x - 10
y3 = x * 10
y4 = x / 10
print ("10을 더하면:", y1)
print ("10을 빼면:", y2)
print ("10을 곱하면:", y3)
print ("10을 나누면:", y4)

x = int(input("정수 입력: "))
y1 = x // 5
y2 = x % 5
print ( x, "나누기 5의 몫은:", y1)
print ( x, "나누기 5의 나머지는:", y2)

x1 = int(input("정수1 입력: "))
x2 = int(input("정수2 입력: "))
y1 = x1 + x2
y2 = x1 * x2
print ("이들의 합은", y1+"이고", "곱은", y2+"입니다." )

#float 실습
x = float(input("실수 입력: "))
print("입력한 실수는", x, "입니다.")

x = float(input("cm 입력:"))
print ("인치로 변환하면", x/2.54, "inch 입니다.")

num1 = int(input("num1 입력: "))
num2 = int(input("num2 입력: "))
num3 = int(input("num3 입력: "))
y1 = num1+num2+num3
y2 = y1 / 3
print("합계는", y1, "이고 평균은", y2, "입니다.")

#방법1
birth = input("생년월일: ")
year = birth[0:4]
month = birth[4:6]
day = birth[6:8]
print("출생일자:", year+"년", month+"월", day+"일")
#방법2
birth = int(input("생년월일: "))
year = birth // 10000
month = (birth % 10000) // 100
day = birth % 100
print("출생일자: ", year, "년", month, "월", day, "일")

#복합대입 연산자
'''
a = a+1 -> a += 1 
+=  -=  *=  /=  //= %=  **=
'''

#관계 연산자(비교 연산자)
'''
== (같다)    != (같지 않다)     >   <   >=  <=

비교의 결과 : True 또는 False (bool형)
주의: => 나 =< 는 없다.
'''

#논리 연산자
'''
a and b : 양쪽 모두 참일 때 True
a or b : 양쪽 중 한쪽만 참이어도 True 
not x : 참과 거짓을 뒤집음

비교의 결과: True 또는 False (bool형)
숫자 0이나 None 값은 False, 그 외 숫자들은 True로 간주함
ex. 0 and ~~ -> False (0은 False로 간주함)
'''
a, b = 10, 0
print (a == b or a > b) #True
print (not b) #True : 숫자 0이나 None 값은 False
print (not a) #False : 그 외 숫자들은 True로 간주하기 때문

year = int(input("연도 입력:"))
ans = ((year%4 == 0) and (year%100 !=0)) or (year%400 == 0)
print("윤년 여부:", ans)

height = float(input("키(cm) 입력: "))
sweight = (height-100)*0.9
print ("표준체중은", sweight, "입니다.")

F = float(input("화씨온도: "))
C = (5/9)*(F-32)
print("섭씨 온도:", C)

x1 = float(input("사각형의 가로: "))
x2 = float(input("사각형의 세로: "))
y1 = x1*x2
y2 = 2(x1+x2)
print("사각형의 넓이는", y1)
print("사각형의 둘레는", y2)

#조건문의 다양한 형태 

#if
#방법1
x = int(input("정수 입력: "))
if (x % 10 != 0):
    print("10의 배수가 아닙니다.")
#방법2
x = int(input("정수 입력: "))
if (not x % 10 == 0):
    print("10의 배수가 아닙니다.")

x = int(input("정수 입력: "))
if x < 100:                      #perl이랑 달리 괄호 없어도 되는구나!
    print("입력한 정수", x, "는 100보다 작음" )
print("프로그램 종료")

x = int(input("정수 입력: "))
if x < 0 : 
    x = -x
print("절대값은", x, "입니다.")

#if-else
x = int(input("정수 입력: "))
if x < 0 :
    print("음수입니다.")
else :
    print("양수입니다.")

x = int(input("정수 입력: "))
if x > 0 :
    if (x % 2) == 0 :
        print("짝수입니다.")
    else :
        print("홀수입니다.")
print("프로그램 종료")

#방법1
print("두 개의 정수를 입력해주세요.")
x1 = int(input("정수1 입력: "))
x2 = int(input("정수2 입력: "))
if x1 >= x2 :
    print("둘 중 큰 수는", x1, "입니다." )
else :
    print("둘 중 큰 수는", x2, "입니다.")
#방법2
ans = 0 #ans가 없는 일이 발생하지 않도록 if 이전에 ans라는 변수를 미리 선언해준다.
print("두 개의 정수를 입력해주세요.")
x1 = int(input("정수1 입력: "))
x2 = int(input("정수2 입력: "))
if x1 >= x2 :
    ans = x1
else :
    ans = x2
print ("둘 중 큰 수는", ans, "입니다.")

print("두 개의 정수를 입력해주세요.")
x1 = int(input("정수1 입력: "))
x2 = int(input("정수2 입력: "))
ans = 0 #변수 미리 선언 해두기 (print할 변수가 없는 것 방지)
if x1 >= x2 :
    ans = x1 - x2
else :
    ans = x2 - x1
print("두 수의 차는", ans, "입니다.")
#일단 빼고 난 다음 --> 음수 이면 양수로 바꿔주는 코딩도 괜찮겠지

x = int(input("정수 입력: "))
if x >= 0 :
    print("양수입니다.")
    if x % 2 == 0 :
        print("짝수입니다.")
    else :
        print("홀수입니다.")
else :
    print("음수입니다.")

x1 = int(input("나이 입력: "))
if x1 >= 20 :
    print("응시 가능")
    x2 = int(input("점수 입력: "))
    if x2 >= 80 :
        print("합격")
    else :
        print("불합격")
else :
    print("응시 불가능")

ans = ""
star = "* * "
print((star*20), "\n 성별과 몸무게, 키에 따른 운동경기 추천 프로그램")
sex = input("성별 입력[남자/여자]: ")
if sex == '남자' :
    weight = float(input("몸무게 입력(kg): "))
    if weight >= 70 :
        ans = "[농구]"
    else :
        ans = "[축구]"
else :
    height = float(input("키 입력(cm): "))
    if height >= 160 :
        ans = "[배구]"
    else :
        ans = "[피구]"
print (ans, "경기를 추천합니다.")

#if-elif-else
score = int(input("점수 입력: "))
if score >=70 :
    print("합격")
elif score >=50: # (score >= 50) and (score < 70)랑 같은 의미 
    print("재시")
else : 
    print("불합격")

score = int(input("점수 입력: "))
grade = 0
if score >= 90 :
    grade = "A"
elif score >= 80 :
    grade = "B"
elif score >= 70 :
    grade = "C"
elif score >= 60 :
    grade = "D"
else :
    grade = "F"
print(grade, "학점")

x = int(input("정수 입력: "))
ans = ""
if x > 0:
    ans = "양수"
elif x < 0:
    ans = "음수"
else :
    ans = "0"
print (x, "는", ans, "입니다.")

x1 = int(input("정수1 입력: "))
x2 = int(input("정수2 입력: "))
if x1 > x2 :
    print("정수1이 정수2보다 큽니다.")
elif x1 < x2 :
    print("정수1이 정수2보다 작습니다.")
else :
    print("두 수는 같습니다.")

#복합조건식
month = int(input("몇 월입니까: "))
if (month >= 3) and (month <= 5) :
    print("봄 입니다.")
elif (month >= 6) and (month <= 8) :
    print("여름 입니다.")
elif (month <= 9) and (month <= 11) :
    print("가을 입니다.")
elif (month == 12) or (month == 1) or (month == 2) :
    print("겨울 입니다.")
else :
    print("그런 월은 없습니다.") #그런 월은 없다는 게 else로 오는 게 간편하겠다!!!

#pass
'''
조건문의 형태는 유지하지만 아무 일도 시키지 않고 싶을 때 사용
-> 나중에 작성해야 할 코드를 표시하는 용도
'''
score = int(input("점수 입력: "))
if score >= 70 :
    pass
elif score >= 50 :
    pass
else :
    pass
