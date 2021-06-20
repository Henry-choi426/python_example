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

# 방법2. sort하여 다르면 추출.
# 테스트는 통과했지만, 미완주 선수가 마지막에 위치한 경우 정답 도출 불가
def solution(participant, completion):

    data = list(zip(sorted(participant),sorted(completion)))
    for a,b in data:
        if a != b:
            return a

# 방법3. sort 후 다르면 추출 및 다 같으면 참여자 중 마지막 값 추출
def solution(participant, completion):

    participant.sort()
    completion.sort()
    for a,b in zip(participant,completion):
        if a != b:
            return a
            
    return participant[-1]
            
