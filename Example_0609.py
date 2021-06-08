"""
- 코딩테스트 연습 - 연습문제 - N개의 최소공배수
- URL : https://programmers.co.kr/learn/courses/30/lessons/42839#

- 문제 분석
모든 경우의 수를 추출 및 중복제거 후 소수 확인
"""
def solution(arr):
    cnt = dict()                    # 최소공배수 결과 dict
    answer = 1
    for i in arr:                   # input list loop
        v = 2                       # 나눠줄 v값
        min = dict()                # 각 숫자 소인수분해 결과값
        while i > 1:                # 숫자값 소인수 분해 완료까지 loop 진행
            if i % v == 0:          # 약수 찾으면
                i = i/v             # i로 나눠주고
                if v in min.keys(): # 해당 인수에 대한 키값이 있으면
                    min[v] +=1      # 밸류값을 하나 더해주고
                else:               # 없으면
                    min[v] = 1      # 생성한다
            else:                   # 약수 못 찾으면
                v += 1              # 나눠주는 값 더해줌
                
        for k,v in min.items():
            if k in cnt.keys():     # 결과 딕셔너리에 해당 키가 있고
                if v > cnt[k]:      # 결과값보다 구한 value가 더 크면 
                    cnt[k] = v      # 밸류 업데이트
            else:
                cnt[k] = v          # 해당키 미 존재시 키와 밸류 추가

    for k, v in cnt.items():        # answer 값 구하기
        answer = answer * k ** v
    return answer

solution([2,6,8,14])