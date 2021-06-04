"""
- 코딩테스트 연습 - 스택/큐 - 프린터
- URL : https://programmers.co.kr/learn/courses/30/lessons/42587

- 문제 분석
queue 형식, location : 몇 번째 출력될건지 확인할 위치
"""
def solution(priorities, location):
    rep = 0
    for i in priorities: # list 갯수 세기(int형이라 loop돌림)
        rep += 1

    st = list(range(rep))

    for i in range(rep-1): # list의 요소들을 확인하여 순서를 재배치
        while True:
            if priorities[i] < max(priorities[i+1:]): # 현재 값보다 큰 값이 있을 경우
                priorities.append(priorities.pop(i)) # 위치변경
                st.append(st.pop(i))
            else:
                break

    answer = st.index(location) + 1 # 인덱스 + 1 해서 순위

    return answer
