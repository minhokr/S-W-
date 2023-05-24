'''
파일 저장 명 : 5장_052_1_최민호.py

작성일 : 2023년 5월 17일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
문제 : 7장 세트와 딕셔너리 
        01. 세트
        
순서가 없으면서 중복을 허용하지 않는 자료구조
'''
# 랜덤으로 로또 번호 알려줘~
# 1. 로또 번호 저장 할 세트 만들기
# 2. 6번 반복하면서
#      1) 1~45 사이의 삽을 세트 변수에 추가
# 3. 로또 번호 출력

# 첫번째는 로또번호가 6개가 안나올수 있음.!
import random
lotto = set()

for i in range(6) :
    lotto.add(random.randint(1,45))
print("lotto  번호 : ", lotto) 

lotto1  = set()
while len(lotto1) != 6 :
    lotto1.add(random.randint(1,45))
print("lotto1  번호 : ", lotto1) 

lotto2 = set()
while True :
    lotto2.add(random.randint(1,45))
    if len(lotto2) == 6 :
        break
print("lotto2  번호 : ", lotto2) 