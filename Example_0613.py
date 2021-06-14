"""
- 백준 - 바이러스
- URL : https://www.acmicpc.net/problem/2606

- 문제 분석
DFS(깊이 우선 탐색)
1번부터 시작하여 감염되는 놈의 갯수
"""

def solution(point,cnt,*line):
    answer = []
    now = 0
    que = [1]
    while len(que)>0:
        answer.append(que[0])   # 왔다 갔다는 걸 넣어줌
        now = que.pop(0)        # 현재 위치 지정
        for i in line:
            if i[0] == now and not i[1] in answer and not i[1] in que:  
                que.append(i[1])
            elif i[1] == now and not i[0] in answer and not i[0] in que: 
                que.append(i[0])
    answer = len(answer) - 1

    return answer

if __name__ == "__main__":
    a = 7
    b = 6
    c = [1,2]
    d = [2,3]
    e = [1,5]
    f = [5,2]
    g = [5,6]
    h = [4,7]
    print(solution(a,b,c,d,e,f,g,h))
    
