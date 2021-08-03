"""
- 코딩테스트 연습 - 탐욕법 - 체육복
- URL : https://programmers.co.kr/learn/courses/30/lessons/42862

- 채점중, 마지막 예제를 실패.
"""


def solution(n, lost, reserve):

    # 체육복을 잃어버리고 여분이 있는 놈들의 리스트
    dumb = list(set(lost).intersection(reserve))

    # 해당 놈들 제거
    for i in dumb:
        reserve.pop(reserve.index(i))
        print("여분 있는데 잃어버린놈 :",lost.pop(lost.index(i)))
        
    answer = n - len(lost)
    
    for per in lost:
        if per-1 in reserve:
            print("빌리는 놈: ",per)
            print("빌려주는 놈: ",reserve.pop(reserve.index(per-1)))
            answer += 1 
        elif per+1 in reserve:
            print("빌리는 놈: ",per)
            print("빌려주는 놈: ",reserve.pop(reserve.index(per+1)))
            answer += 1 
            
    return answer

print(solution(5,[2,3,4],[1,3,5]))