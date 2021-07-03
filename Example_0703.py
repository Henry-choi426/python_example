"""
- 백준 - 팩토리얼
- URL : https://www.acmicpc.net/problem/10872

- 문제 분석
재귀함수를 활용하여 팩토리얼 만들기.
"""

def solution(number):
    if number == 1:
        return 1
    else:
        return solution(number-1)*number


solution(10)
# 3628800