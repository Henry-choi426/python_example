"""
- 코딩테스트 연습 - 정렬 - 삼각 달팽이
- URL : https://programmers.co.kr/learn/courses/30/lessons/68645

- 문제 분석
반시계 방향으로 도는 숫자열의 흐름을 이중 loop를 통해 구현
"""
# ver.01 시간초과
def solution(n):
    answer = []
    cnt = 0
    data = []
    for i in range(1,n+1): # 총 갯수
        cnt += i
        data.append([0]*i) # n 갯수만큼 층을 생성

    for i in range(1,cnt+1): # 갯수만큼 list요소 생성
        answer.append(i)
    
    m = n
    lo = 0
    
    while True:
        
        if m == 0:
            break
        for i in range(lo*2,n-lo): # 각 층의 첫번째 요소 채우기
            data[i][lo] = answer.pop(0)
        m = m-1

        if m == 0:
            break
        for i in range(1+lo,n-lo*2): # 마지막 층의 요소 채우기
            data[n-1-lo][i] = answer.pop(0)
        m = m-1

        if m == 0:
            break
        for i in range(n-2-lo,lo*2,-1): # 각 층의 마지막 요소 채우기, 
            data[i][-1-lo] = answer.pop(0)
        m = m-1
        lo += 1 
        
    for i in range(n):
        for v in range(i+1):
            answer.append(data[i][v])

    return answer
print(solution(8))

# ver.02 컴프리헨션 및 sum 함수를 사용했지만, 그래도 시간 초과 . .
def solution(n):
    answer = []
    cnt = 0
    data = []
    for i in range(1,n+1): # 총 갯수
        cnt += i
        data.append([0]*i) # n 갯수만큼 층을 생성

    answer = [x for x in range(1,cnt+1)]
        
    m = n
    lo = 0
    while True:
        
        if m == 0:
            break
        for i in range(lo*2,n-lo): # 각 층의 첫번째 요소 채우기
            data[i][lo] = answer.pop(0)
        m = m-1

        if m == 0:
            break
        for i in range(1+lo,n-lo*2): # 마지막 층의 요소 채우기
            data[n-1-lo][i] = answer.pop(0)
        m = m-1

        if m == 0:
            break
        for i in range(n-2-lo,lo*2,-1): # 각 층의 마지막 요소 채우기, 
            data[i][-1-lo] = answer.pop(0)
        m = m-1
        lo += 1 
        
    answer = sum(data,[])

    return answer
print(solution(100))