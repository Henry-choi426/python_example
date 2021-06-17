"""
- 코딩테스트 연습 - KAKAO BLIND RECRUITMENT - [1차] 비밀지도
- URL : https://programmers.co.kr/learn/courses/30/lessons/17681

- 문제 분석
각각의 입력받은 리스트를 loop 돌려 이진화 시킨 후, 각 자리별 숫자 합으로
answer 도출
"""
def make(z,x): # 주어진 한 변의 크기만큼 데이터 가공
    z = list(str(bin(z)))
    z.pop(1)
    while True:
        if len(z) > x:
            z.pop(0)
        elif len(z) < x:
            z.insert(0,'0')
        else:
            break
    return z

def solution(n, arr1, arr2):
    answer = ['']*n
    floor = 0
    data= list(zip(arr1, arr2))

    for a,b in data:
        a = make(a,n)
        b = make(b,n)
        c = list(zip(a,b))

        for d,e in c:
            if int(d)+int(e) > 0:
                answer[floor] += '#'
            else:
                answer[floor] += ' '
                
        floor += 1
        
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))