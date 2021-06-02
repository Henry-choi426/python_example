"""
- 코딩테스트 연습 - 스택/큐 - 다리를 지나는 트럭
- URL: https://programmers.co.kr/learn/courses/30/lessons/42583

"""

len = 2
wei = 10
twei = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = [0] * bridge_length # 다리 길이만큼 que생성
    while truck_weights or sum(que) != 0: # 트럭 list가 비고 다리 위에 차가 없을때 loop 종료
        answer += 1
        que.pop(0)
        if truck_weights: # 더 뺄 차가 있을 경우
            if truck_weights[0] + sum(que) <= weight:
                que.append(truck_weights.pop(0)) # 다리위에 트럭 올리기
            else:
                que.append(0)
    
    return answer
        
print(solution(len,wei,twei))