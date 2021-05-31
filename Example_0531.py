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
