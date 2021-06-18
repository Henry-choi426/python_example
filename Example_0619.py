"""
- 백준 - Hashing
- URL : https://www.acmicpc.net/problem/15829

- 문제 분석
문자열의 유니코드를 추출하여 정수화 시켜 답 만들기
"""
def solution(numbers, target):

    answer = 0
    idx = 0
    data = list(target)
    for i in data:
        answer += (ord(i)-96) * 31 ** idx
        idx+=1
    answer = answer % 1234567891
    return answer

print(solution(5, 'abcde'))
print(solution(5, 'zzz'))
print(solution(5, 'i'))