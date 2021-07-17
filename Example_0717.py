"""
- 코딩테스트 연습 - Summer/Winter Coding(~2018) - 배달
- URL : https://programmers.co.kr/learn/courses/30/lessons/12978
"""


# 기존 road를 index에 맞추는 Fucntion
def cube(x):
    x[0], x[1] = x[0]-1, x[1]-1
    return x


def solution(N, road, K):

    costs = list(map(cube, road))

    answer = 0
    visited = [False for _ in range(N)]
    cost = [500001 for _ in range(N)]
    visited[0] = True
    cost[0] = 0
    
    # 시작점에서 먼저 비용 계산
    checkLoc = 0
    for v1,v2,c in road:
        if v1 == checkLoc and visited[v2] == False: #
            cost[v2] = min(cost[v2],cost[v1]+c)
        if v2 == checkLoc and visited[v1] == False: #
            cost[v1] = min(cost[v1],cost[v2]+c)

    # 방문하지 않은 노드가 있다면 방문하지 않은 지역중 최솟값 찾기.
    while False in visited:
        checkLoc = -1
        CheckValue = 500001

        # 방문하지 않은 지역 중 최솟값 찾기
        for i in range(N):
            if visited[i] == False and cost[i] < CheckValue:
                checkLoc = i
                CheckValue = cost[i]

        # 방문하지 않은 지역이 없으면 while문 탈출
        if checkLoc == -1:
            break

        # 해당 지역에서의 최솟값 추출
        visited[checkLoc] = True
        for v1, v2, c in road:
            if v1 == checkLoc and visited[v2] == False:
                cost[v2] = min(cost[v2], cost[v1]+c)
            if v2 == checkLoc and visited[v1] == False:
                cost[v1] = min(cost[v1], cost[v2]+c)
    
    # 최대배달거리 이하인 거리만 추출
    for i in cost:
        if i <= K:
            answer += 1

    return answer

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
             [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))