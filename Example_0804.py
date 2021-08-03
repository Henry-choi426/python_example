"""
- 백준 - 전자레인지
- URL : https://www.acmicpc.net/problem/10162
"""

seconds = int(input())

if seconds % 10 != 0:
    print(-1)
else:
    s300 = seconds // 300 
    s60 = (seconds % 300) // 60
    s10 = (seconds % 300) % 60 //  10 
    
    print(s300," ",s60," ",s10)
