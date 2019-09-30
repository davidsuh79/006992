################
## LISTING 11.1
################
print("hello!")                           #A
print(3*2*(17-2.1))                       #B
print("abc"+"def")                        #C
word = "art"                              #D
print(word.replace("r", "n"))             #E
#A 문자열
#B 수학 식
#C 두 문자열 연결하기
#D 변수 만들기
#E "r"을 "n"으로 바꾸기


################
## LISTING 11.2
################
a = 1                                     #A
b = 2                                     #A
c = a/b                                   #B
print(a,"/",b,"=",c)                      #C

add = str(a)+"/"+str(b)+"="+str(c)        #D
print(add)                                #E
#A 변수 초기화
#B 나누기 계산
#C 콤마를 사용해 정수(변수 a,b,c)와 문자열("/", "=")을 분리
#D str을 사용해 정수를 문자열로 변환한 후 + 연산자로 "/"과 "=" 문자열과 연결
#E 문자열 출력



################
## LISTING 11.3
################
input("어디에 사십니까? ")              #A
print("나는 곡성에 삽니다.")            #B
#A 사용자에게 프럼프트를 표시해서 입력 요청. 이 부분에서 프로그램은 사용자가 입력을 마칠 때까지 실행을 잠시 멈춤
#B 사용자가 엔터를 누르면 이 줄이 실행되고 프로그램이 끝남


################
## LISTING 11.4
################
user_place = input("어디에 사십니까? ")             #A
text = user_place.capitalize() + "!"              #B
print(text)                                       #C
print("거기는 참 좋은 곳이라지요!")                  #C
#A 사용자 입력을 받고 그 값을 user_place 변수에 저장
#B 사용자 입력에서 첫 글자를 대문자로 만든 문자열과 느낌표 하나로 이뤄진 문자열을 연결
#C 사용자 입력에 따라 적합한 출력을 표시

################
## LISTING 11.5
################
user_input = input("제곱을 계산할 수를 입력하시오: ")                #A
num = int(user_input)                                            #B
print(num*num)                                                   #C
#A 사용자 입력을 받아서 저장
#B 사용자 입력을 정수로 변환
#C 정수 값의 제곱을 계산해 출력. 이 프로그램의 첫 두 줄을 num = int(input("제곱을 계산할 수를 입력하시오: "))라는 한 줄로 바꿀 수도 있음

################
## LISTING 11.6
################
num1 = float(input("첫번째 수를 입력하시오: "))                #A
num2 = float(input("두번째 수를 입력하시오: "))                #B
print(num1, "*", num2, "=", num1*num2)                      #C
#A 수를 입력받아서 실수(float)로 바꿈
#B 다른 수를 입력 받아서 실수(float)로 바꿈
#C 사용자가 입력한 두 실수와 결과를 예쁘게 출력
