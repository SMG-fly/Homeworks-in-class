#예외 처리
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:
    print('예외가 발생했습니다.')
    
#특정 예외만 처리하기 - 예외 유형별 처방
'''
try:
    실행할 코드
except 예외 이름:
    예외가 발생했을 때 처리하는 코드
    
예외 이름 예시 : ZeroDivisionError, ValueError
'''
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except ZeroDivisionError:
    print ('0으로는 나눌 수 없습니다.')
except ValueError: #숫자가 들어갈 곳에 str 등이 들어갈 경우 나오는 에러
    print ('숫자를 넣으세요.')

#예외의 에러 메세지 받아오기
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except ZeroDivisionError as e:
    print('0으로는 나눌 수 없습니다.', e)
except ValueError as e:
    print('숫자를 넣으세요.', e)
    
#모든 예외의 에러 메세지 받아오기
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except Exception as e:
    print('예외가 발생했습니다.', e)

#다중 예외 처리 구조
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except Exception as e: #예외가 발생했을 때 처리하는 코드
    print ('예외가 발생했습니다.', e)
else: #예외가 발생하지 않았을 때 실행할 코드
    print(y)

#다중 예외 처리 구조 - finally    
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except Exception as e:
    print('예외가 발생했습니다.', e)
else:
    print(y)
finally: #예외 발생 여부와 상관없이 항상 실행할 코드
    print('코드 실행 종료')

#사용자 지정 예외 발생시키기
#raise 예외('에러메세지')
#5의 배수가 아니면 예외 발생
try: 
    x = int(input('5의 배수를 입력: '))
    if x % 5 != 0:
        raise Exception('5의 배수가 아님!!!') #예외 발생 #Exception 대신 ZeroDivisionError 해도 똑같이 돌아감 #단
    print (x)
except Exception as e: #사용자 정의 포함, 모든 예외 발생시 이 코드 실행
    print('예외 발생:', e) #5의 배수가 아닐 때는 e 메세지로 '5의 배수가 아님!!!'이 출력된다.
    
#예외와 함수
#함수 안에서 예외 처리한 경우
def five_multiple():
    try:
        x = int(input('정수 입력: '))
        print(x)
    except Exception as e:
        print('예외 발생:', e)
    
five_multiple()

#함수 안 예외를 상위로 넘긴 경우
def five_multiple():
    x = int(input('정수 입력: '))
    print(x)
    
try:
    five_multiple()
except Exception as e:
    print('예외 발생:', e)
    
#raise를 사용해서 함수 안에서 사용자 예외를 발생시키고 상위에서 처리 가능
def five_multiple():
    x = int(input('5의 배수를 입력: '))
    if x % 5 != 0:
        raise Exception('5의 배수가 아님!!!')
    print(x)

try:
    five_multiple()
except Exception as e:
    print('예외 발생:', e)

#현재 예외를 다시 발생시키기
#함수 안에서 예외 처리를 했지만 상위 코드 블록에서도 같은 예외 처리를 또 하도록
#즉, 한 문제에 대해 같은 에러 메세지를 도출하도록
def five_multiple():
    try:
        x = int(input("5의 배수를 입력: "))
        if x % 5 != 0:
            raise Exception('5의 배수가 아님!!!!')
        print(x)
    except Exception as e:
        print('함수 안에서 예외 발생:', e)
        raise #raise로 현재 예외를 다시 발생  -> 상위에 넘김
    
try:
    five_multiple()
    a = 10 / 0
except Exception as e:
    print('스크립트 파일에서 예외 발생:', e)
    
#실습
def divide(x, y):
    try:
        ans = x / y
    except ZeroDivisionError as e: #함수 안
        print('0으로 나눌 수 없음.', e)
        raise
    else:
        print(ans)   

try:
    x = int(input('x: '))
    y = int(input('y: '))
    divide(x, y)
except ValueError as e:
    print('숫자를 넣으세요', e)
except ZeroDivisionError as e: #함수 안
    print('함수 안에서 예외 발생:', e)
finally:
    print('프로그램 종료')
    