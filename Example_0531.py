#  코딩테스트 연습 - 스택/큐 - 주식가격

prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []
    # prices 배열의 현재값을 위한 변수 i
    for i in range(len(prices)):
        sec = 0

        # i와 미래를 비교하기 위한 v
        for v in range(i+1,len(prices)+1):
            

            if v == len(prices): # 총 시간과 반복이 일치할 경우
                answer.append(sec)
                break
            elif prices[i] > prices[v]: # 현재 가격이 미래보다 클 경우 초를 추가 후 어팬드
                sec += 1
                answer.append(sec)
                break
            elif prices[i] <= prices[v]: # 미래보다 현재 가치가 더 낮으면 초 추가 후 다음 반복 수행
                sec += 1

    return answer

print(solution(prices))

# 방법 2. 코드 간소화

def solution2(prices):

    rep = len(prices)
    answer = [0] * rep

    for v in range(rep):
        for i in range(v+1,rep):
            answer[v] += 1
            if prices[i] < prices[v]: # 미래가 현재보다 작은 경우 
                break
            
    return answer

print(solution2(prices))


"""
- 코딩테스트 연습 - 스택/큐 - 기능개발
- URL: https://programmers.co.kr/learn/courses/30/lessons/42586

- 문제해석
기능별 개발 속도가 다르고, 뒤에 기능이 먼저 개발되도 앞에 기능이 배포될 때
같이 배포되기 때문에 QUEUE 접근
"""
pro1 = [93, 30, 55]
spd1 = [1, 30, 5]

pro2 = [95, 90, 99, 99, 80, 99]
spd2 = [1, 1, 1, 1, 1, 1]

def solution3(progresses, speeds):
    answer = [] # 결과값 리스트 선언

    while progresses:
        cnt = 0     # 카운트 변수 선언
        progresses = [x+y for x,y in zip(progresses, speeds)] # 진행상황에 속도 더함

        while progresses:
            if progresses[0] >= 100:    # 첫 idx가 진행상황 100 넘길때
                cnt += 1                # 갯수를 더하고
                progresses.pop(0)       # pop으로 추출
                speeds.pop(0)
            elif cnt > 0:               # idx 0이 100이 안넘고 갯수가 있는 경우 append
                answer.append(cnt)      
                break
            else:                       # idx 0이 100을 안넘고 갯수도 없는 경우 loop문 나옴
                break
            
    answer.append(cnt)                  # loop문 종료 후, 마지막 cnt는 진행중인 프로그램이 없어서
                                        # 하지못한 append를 마지막으로 실행
    return answer

print(solution3(pro1,spd1)) # [2,1]
print(solution3(pro2,spd2)) # [1,3,2]
