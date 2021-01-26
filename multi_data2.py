hobby = []
hobby.append('코딩')
print('갯수>>',len(hobby))
hobby.append('등산')
print('갯수>>',len(hobby))
#처음에 append를 이용하여 2개의 데이터를 직접 입력하였고,

for _ in range(3):
    data = input('당신의 새로운 취미는>> ')
    hobby.append(data)
#그 다음 for문에서 횟수를 3번으로 추가로 입력하여서 데이터 5개의 결과가 나왔다.
print('갯수>>', len(hobby))

for x in hobby:
    print(x, end=' ')
#for-each의 경우 데이터의 마지막까지 반복하기 때문에,
#앞의 hobby에 저장된 데이터 총 5개를 꺼내와서 줄바꿈 없이 모두 출력하였다.