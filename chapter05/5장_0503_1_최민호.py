'''
파일 저장 명 :  5장_0503_1__최민호.py
작성일 : 2023년 5월 3일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 사용자로부터 정수를 입력받아
       해당 단의 구구단을 출력하는 프로그램을 작성하시오.
       
[문제 분석]
    사용자로 부터 dan 입력 받는다.
    곱하는 수 : su
    
    입력받은 단은 고정이다.
    곱하는 수는 1부터 9까지 1씩 증가한다.
'''

#알고리즘 for  
#1. 사용자로부터 단을 입력 받는다.
#2. 곱하는 수는 1부터 9까지 반복하면서
#   1) 구구단을 출력한다.

print("for 반복문으로 구구단을 출력하세요.")
dan = int(input("알고 싶은 단을 입력하세요. : "))

print(":: {} 단 ::" .format(dan))
for num in range(1, 10) :
    print("{} X {} = {}" .format(dan,num,dan*num))


#알고리즘 whlie
#1. 사용자로부터 단을 입력 받는다.
#2. 곱하는 수는 1부터
#3. 곱한는 수가 9까지 반복하면서
#   1)구구단을 출력
#   2)곱하는 수 1씩 증가

dan = int(input("알고 싶은 단을 입력하세요. : "))

num = 1

while num <= 9 :
    print("{} X {} = {}" .format(dan,num,dan*num))
    num = num + 1