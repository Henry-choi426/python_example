"""
- 코딩테스트 연습 - 완전 탐색 - 소수찾기
- URL : https://programmers.co.kr/learn/courses/30/lessons/42839#

- 문제 분석
모든 경우의 수를 추출 및 중복제거 후 소수 확인
"""
from itertools import permutations as per

def check(n):
    
    if n < 2: # 1 이하 숫자 거르기
        return False
    
    for v in range(2,(n//2)+2): # 2이상의 소수 판단
        if n % v == 0:
            return False
    return True

def solution(numbers):
    
    answer = []
    for k in range(1, len(numbers)+1): # 1부터 숫자의 길이만큼 반복
        perlist = list(map(''.join, per(list(numbers), k))) #k자리 경우의 수 추출
        for i in list(set(perlist)): # set과 list화로 1차 중복제거
            if check(int(i)): # 소수 맞으면 
                answer.append(int(i))  # answer에 어펜드

    answer = len(set(answer)) # 2차 중복제거 및 숫자 확인

    return answer

print(solution('17'))