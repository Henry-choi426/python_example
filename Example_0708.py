"""
- 백준 - 동적계획법 - 계단오르기
- URL : https://www.acmicpc.net/problem/2579

- 문제 풀이 과정 : 한 번에 한 계단, 혹은 두 계단씩 오를 수 있으므로 매번 계단수 마다의 최대값을 answer list에 저장.
                  for 문으로 전전 최댓값 + 현재 계단점수 와 전 최댓값을 비교하여 더 큰 값을 저장
                  마지막 계단은 무조건 밟아야 하므로, input list를 reverse시켜 무조건 밟고 시작하기

"""
def solution(floor):

    answer = [] # 시작점 점수
    floor.reverse() # 마지막 도착 계단을 무조건 밟아야 하므로 뒤에서부터 내려오기
    answer.append(floor[0]) # 도착 지점의 계단값으로 sum의 최댓값 미리 넣어주기 
    
    answer.append(floor[0]+floor[1])
    answer.append(max(floor[0]+floor[2],floor[1]+floor[2]))
    
    print(answer)
    
    for i in range(3,len(floor)):
        answer.append(max(answer[i-2]+floor[i],answer[i-3]+floor[i-1]+floor[i]))
    print(answer)
    print(floor)
    return answer[-1]
    
print(solution([6,10,20,15,25,10,20])) # 76
