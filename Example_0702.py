"""
- 백준 - 이진수 변환
- URL : https://www.acmicpc.net/problem/10829

- 문제 분석
재귀함수를 활용하여 이진수로 변환하기.
"""

def solution(number):
    if number == 1:
        return "1"
    else:
        if int(number) % 2 == 1: # 홀수일 때
            return solution(number//2)+'1'
        else:
            return solution(number//2)+'0'
        
solution(53)
# '110101'