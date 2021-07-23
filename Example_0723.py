"""
- 백준 - 특정 거리의 도시 찾기
- URL : https://www.acmicpc.net/problem/18352
"""

# 기존 road를 index에 맞추는 Fucntion
def cube(x):
    x[0], x[1] = x[0]-1, x[1]-1
    return x

def solution(base,road):
    
    costs = list(map(cube, road))
    
    N = base[0]
    K = base[2]
    start = base[3]-1
    
    answer = []
    visited = [False for _ in range(N)]
    cost = [500001 for _ in range(N)]
    
    visited[start] = True
    cost[start] = 0
    
    # 시작점에서 먼저 비용 계산
    checkLoc = start
    for v1,v2 in road:
        if v1 == checkLoc and visited[v2] == False: #
            cost[v2] = min(cost[v2],cost[v1]+1)
        if v2 == checkLoc and visited[v1] == False: #
            cost[v1] = min(cost[v1],cost[v2]+1)

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
        for v1, v2 in road:
            if v1 == checkLoc and visited[v2] == False:
                cost[v2] = min(cost[v2], cost[v1]+1)
            if v2 == checkLoc and visited[v1] == False:
                cost[v1] = min(cost[v1], cost[v2]+1)
    
    # 지정 거리만 추출
    c = np.array(cost)
    answer = np.where(c == K)[0]
    if len(answer) == 0:
        print(-1)
    else:
        for i in answer:
            print(i+1)

solution([4,4,2,1],[[1,2],[1,3],[2,3],[2,4]])
solution([4,4,1,1],[[1,2],[1,3],[2,3],[2,4]])