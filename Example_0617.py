"""
- 백준 - 진법 변환
- URL : https://www.acmicpc.net/problem/5692

- 문제 분석
문자열의 유니코드를 추출하여 정수화 시켜 답 만들기
"""
def solution(numbers, target):
    answer = 0
    idx = 0
    data = list(numbers)
    for i in data[::-1]:
        if i.isalpha(): # 알파벳인 경우 유니코드를 추출 후 연산
            answer += (ord(i)-55) * target ** idx
            idx += 1
        else: # 숫자인 경우 바로 연산
            answer += int(i) * target ** idx
            idx += 1  

    return answer
solution('ZZZZZ', 36) # 60466175
