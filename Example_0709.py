"""
- 코딩테스트 연습 - 동적계획법 - 정수 삼각형
- URL : https://programmers.co.kr/learn/courses/30/lessons/43105

- 문제 풀이 과정 : 미리 1층 값 부여 후 경우의 수에 맞게 최댓값 APPEND.

"""

def solution(triangle):
    answer = [triangle[0]]
    floor = 1

    for i in triangle[1:]:
        p = []
        
        for a in range(floor+1):
            if a == 0:
                p.append(answer[floor-1][0]+i[0])
            elif a == floor:
                p.append(answer[floor-1][-1]+i[-1])
            else:
                p.append(max(answer[floor-1][a-1]+i[a],answer[floor-1][a]+i[a]))
                
        answer.append(p)
        floor += 1

    return max(answer[-1])

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
# 30