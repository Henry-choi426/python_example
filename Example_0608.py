"""
- 백준 - 숫자 카드 2
- URL : https://programmers.co.kr/learn/courses/30/lessons/42839#

- 문제 분석
띄어쓰기로 구분된 데이터를 split하여 해당 count한다.
"""
def solution(a,b,c,d):
    answer = ''
    n_card = b.split(' ')
    m_card = d.split(' ')
    
    for v in m_card:
        answer = answer + ' ' + str(n_card.count(v))
    
    return answer

n = 10
nc = '6 3 2 10 10 10 -10 -10 7 3'
m = 8
md = '10 9 -5 2 3 4 5 -10'

print(solution(n,nc,m,md))