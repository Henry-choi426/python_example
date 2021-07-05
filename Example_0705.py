"""
- 코딩테스트 연습 - 2020 KAKAO BLIND RECRUITMENT - 괄호변환
- URL : https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

- 문제 풀이 과정 : 재귀함수를 활용, 함수의 모듈화를 통해 코드 복잡성 낮춤

                  먼저 INPUT 인 P 가 무조건 균형잡힘.
                  두 문자열로 나눌 때 하나의 균형이 잡히기 위해선 무조건 짝수 단위로 분할
                  올바른 문자열 체크시 LOOP 를 통해 )가 ( 보다 먼저 많이 나오면 올바른 문자열이 아님
"""

def b_check(d): # 균형잡힌 문자열 체크 로직
    if d.count('(') == d.count(')'): 
        return True
    else:
        return False
    
def p_check(c): # 올바른 문자열 체크 로직
    a = 0
    for i in list(c):
        if i == '(': # 더하기
            a += 1
        elif i == ')': # 빼기
            a = a - 1
            if a < 0:
                return False
    return True

def dev(c): # 문자열 나누기
    cnt = len(c)
    for i in range(2,cnt+1,2): # 짝수개로 짤라 균형잡힌지 확인
        if b_check(c[:i]):
            return c[:i],c[i:]
            

def solution(p):
    # 1.빈 문자열이면 빈 문자열 반환
    if not p: 
        return '' 
    
    # 2. 빈 문자열이 아니라면 두 문자열로 나누기.
    u, v = dev(p) 
    
    # 3. u가 올바른 문자열이면 u에 붙인 후 반환
    if p_check(u): 
        return u + solution(v)
    
    # 4. u가 올바른 문자열이 아니라면
    else: 
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
                
        return answer