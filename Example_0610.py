"""
- 백준 - DFS와 BFS
- URL : https://www.acmicpc.net/problem/1260

- 문제 분석
DFS(깊이 우선 탐색)

"""

# 깊이 우선 탐색(DFS)
def solution(st,*line1):

    line = list(line1)
    # 내림차순으로 검색해야 하니 sort 실행
    line.sort(key = lambda a: (a[0], a[1]))
    answer = []
    now = 0
    que = [st[2]]
    while len(que) > 0:
        answer.append(que[-1])   # 왔다 갔다는 걸 넣어줌
        now = que.pop(-1)        # 현재 위치 지정
        stay = []
        for i in line:
            # 현재 위치가 맞고(i[0]==now) 길이 방문하지 않았고(not in answer) 
            if i[0] == now and not i[1] in answer:  
                if not i[1] in que: # 갈 예정이 아니라면(not in que) que에 추가 및 answer에 담기
                    stay.append(i[1])
                else: # 갈 예정에 있지만 깊이 탐색 필요한 경우, 기존껄 앞으로 보내기. 
                    stay.append(que.pop(que.index(i[1])))
            elif i[1] == now and not i[0] in answer: 
                if not i[0] in que:
                    stay.append(i[0])
                else:
                    stay.append(que.pop(que.index(i[0])))
        stay.sort(reverse=True)
        for v in stay:
            que.append(v)
    return answer
     


# 너비우선탐색(BFS)
def solution1(st,*line):
    
    answer = []
    now = 0
    que = [st[2]]
    while len(que)>0:
        answer.append(que[0]) # 왔다 갔다는 걸 넣어줌
        now = que.pop(0) # 현재 위치 지정
        stay = []
        for i in line:
            # 현재 위치가 맞고(i[0]==now) 길이 방문하지 않았고(not in answer), 갈 예정이 아니라면(not in que) que에 추가 및 answer에 담기
            if i[0] == now and not i[1] in answer and not i[1] in que:  
                stay.append(i[1])
            elif i[1] == now and not i[0] in answer and not i[0] in que: 
                stay.append(i[0])
        # 내림차순으로 검색해야 하니 sort 실행
        stay.sort()
        for v in stay:
            que.append(v)
    return answer

if __name__ == "__main__":
    a =[5,5,3]
    b=[5,4]
    c=[5,2]
    d=[1,2]
    e=[3,4]
    f=[3,1]
    print(solution(a,b,c,d,e,f))
    print(solution1(a,b,c,d,e,f))
    a =[4,5,1]
    b=[1,2]
    c=[1,3]
    d=[1,4]
    e=[2,4]
    f=[3,4]
    print(solution(a,b,c,d,e,f))
    print(solution1(a,b,c,d,e,f))

    print(solution([1000,1,1000],[999,1000]))
    print(solution1([1000,1,1000],[999,1000]))

