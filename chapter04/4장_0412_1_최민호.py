'''
작성일 : 2023년 4월 12일
학과 : 컴퓨터공학부
학번 : 202395032
이름 : 최민호
설명 : 입력 받은 정수가 양수인지, 음수인지 0인지 판단하시오.
'''
#1. 정수를 입력 받는다.
num = int(input("정수를 입력하세요"))
#2. 만약 입력받은 정수가 0보다 크면
#   1)"00은 양수입니다"
if num > 0 :
    print(num,"은(는) 양수입니다")
#3. 만약 입력받은 정수가 0보다 작으면
#   1)"00은 음수입니다"
elif num < 0 :
    print(num,"은(는) 음수입니다")
#4. 아니면 
#   1)0입니다
else :
    print(num,"입니다")