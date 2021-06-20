"""
- 코딩테스트 연습 - 해시 - 완주하지 못한 선수
- URL : https://programmers.co.kr/learn/courses/30/lessons/42576
"""

# 방법 1. 완주자를 loop 돌려 참가자에 없으면 return. 
# 정확성 테스트는 통과했지만 효율성 통과 실패

def solution(participant, completion):

    answer = ''
    for i in completion:
        if i in participant:
            completion.pop(completion.index(i))
        else:
            answer = i
            break
            
    return answer