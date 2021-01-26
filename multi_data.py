food = ['아이스크림','아이스아메리카노','생수'] #목록(list)
# hobby = []
print(food [0])
print(food [1])
print(food [2])
# 첫번쨰 음식, 두번째 음식, 세번째 음식 각각 출력하기
for i in range(0, 3):
    print(food[i],end=' ')
#각각의 음식을 for문을 이용하여 range에 지정한 횟수인 0부터 시작해서 3번 출력하기
print()
for x in food: #'for-each' 처음부터 끝까지 알아서!
    print(x, end=' ')
#각각의 음식을 for-each를 이용하여 모두 출력하기
print()

# 오늘 끝나고 나서, 할 일 5가지를 목록으로 만들어보세요.
# 2가지 방식으로 프린트

after = ['1.마트 가기','2.저녁 먹기','3.복습 하기','4.샤워 하기','5.게임 하기']

for i in range(0, 5):
    print(after[i], end=' ')
#오늘의 할일을 for문을 이용하여 지정한 횟수인 5번 출력하기
print()
for y in after:
    print(y, end=' ')
#오늘의 할일을 for-each를 이용하여 모두 출력하기
print()
print('목록의 갯수는',len(after),'개')
#목록의 갯수는 len을 이용하여 결과값을 도출하였다.