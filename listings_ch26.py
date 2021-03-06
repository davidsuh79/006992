################
## LISTING 26.1
################
heights = [1.4, 1.3, 1.5, 2, 1.4, 1.5, 1]
heights.reverse()                                 #A
print(heights)                                    #B
heights.sort()                                    #C
print(heights)                                    #D
heights.reverse()                                 #E
print(heights)                                    #F
#A 원래 리스트를 역순으로 만듦
#B 원래 리스트를 역순으로 만들었기 때문에 [1, 1.5, 1.4, 2, 1.5, 1.3, 1.4]를 출력
#C 리스트를 오름차순으로 정렬
#D 리스트를 오름차순으로 정렬했기 때문에 [1, 1.3, 1.4, 1.4, 1.5, 1.5, 2]를 출력
#E 정렬된 리스트를 역순으로 만듦
#F 오름차순 정렬된 리스트를 역순으로 만들었기 때문에 [2, 1.5, 1.5, 1.4, 1.4, 1.3, 1]를 출력





################
## LISTING 26.2
################
L = [[], [], []]           #A
L[0] = [1,2,3]             #B
L[1].append('t')           #C
L[1].append('o')           #D
L[1][0] = 'd'              #E
#A 빈 리스트로 이뤄진 리스트를 만듦
#B 0번 인덱스에 있는 리스트를 [1, 2, 3]으로 설정했으므로 L의 값은 [[1,2,3], [], []]
#C 중간에 있는 리스트에 ’t’라는 문자열을 넣었으므로 L의 값은 [[1,2,3], ['t'], []]
#D 중간에 있는 (한번 내용이 변경된) 리스트에 ’o’라는 문자열을 덧붙었으므로 L의 값은 [[1,2,3], ['t', 'o'], []]
#E 중간에 있는 (값이 바뀐) 리스트의 0번 인덱스에 있는 문자열을 ’d’로 바꿨으므로 L의 값은 [[1,2,3], ['d', 'o'], []]




################
## LISTING 26.3
################
x = 'x'                                         #A
o = 'o'                                         #B
empty = '_'                                     #C

board = [[x, empty, o], [empty, x, o], [x, empty, empty]]   #D
#A 변수 x
#B 변수 o
#C 빈 칸
#D 각 변수에 값이 정해져 있으므로, board라는 변수에는 세 줄(하위 리스트가 각 줄을 표현)과 세 열(하위 리스트 안의 3개의 원소가 각각의 열을 표현)이 있음


################
## LISTING 26.4
################
stack = []                                                #A
cook = ['ㅎ', 'ㅎ', 'ㅎ']                                  #B
stack.extend(cook)                                        #C
stack.pop()                                               #D
stack.pop()                                               #D
cook = ['ㄱ', 'ㄱ']                                       #E
stack.extend(cook)                                        #F
stack.pop()                                               #D
cook = ['ㅎ', 'ㅎ']                                       #E
stack.extend(cook)                                        #F
stack.pop()                                               #D
stack.pop()                                               #D
stack.pop()                                               #D
#A 빈 리스트
#B 부침개 3개 부침
#C 이모가 부친 부침개를 스택에 (순서대로) 추가
#D 스택(리스트)의 마지막 원소 제거
#E 새로 부친 부침개 한무더기
#F 스택 끝에 부침개 더미 추가




################
## LISTING 26.5
################
line = []                  #A
line.append('오현석')       #B
line.append('이계영')       #C
line.pop(0)                #D
line.append('이일민')       #E
line.append('김도남')       #E
line.pop(0)                #F
line.pop(0)                #F
line.pop(0)                #F
#A 빈 리스트
#B 이제 큐에 1명이 들어있음
#C 이제 큐에 2명이 들어있음
#D 큐의 첫번째 사람 제거
#E 새로운 사람을 큐(리스트) 맨 뒤에 추가
#F 사람을 제거할 때는 큐(리스트) 맨 앞부터 제거
