"""
- 백준 - 팩토리얼 진법
- URL : https://www.acmicpc.net/problem/5692

- 문제 분석

"""
# 팩토리얼 생성 로직
def fac(a):
    answer = 1
    for i in range(2,a+1):
        answer = answer*i
    return answer
    
# 정답 도출
def solution(num):
    answer = 0
    num = list(str(num))    # input을 list화
    for i in range(1,len(num)+1): 
        answer += int(num[-i]) * fac(i) # 인덱스를 역으로 받아 자리수에 맞게 loop
    
    return answer

print(solution(719)) # 53