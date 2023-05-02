'''
파일 저장 명 :  5장_0502_1__최민호.py
작성일 : 2023년 5월 2일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 사용자로부터 정수를 입력받아 
       1부터 입력 받은 수까지의 합계를 계산하시오.
       
[문제 분석]
합계 = 합계 +수
합계 = 0
1부터 입력 받은 수 까지 반복하면서

변수 : num, sum, imtput_num
'''
#알고리즘
#1. 정수 입력 받기
#2. 합계는 0
#3. 수는 1부터
#4. 수는 입력 받은 수까지 반복하면서
#   1)합계 계산
#   2)수는 1씩 증가
#5. 합계 출력

input_num = int(input("정수 입력 : "))

sum = 0
num = 1   #초기값(시작값)

while num <= input_num :   #조건식(종료값)
    sum = sum + num
    num = num + 1   #증감식이 없으면 무한반복한다.

print("1부터 {}까지 의 합 : {}" .format(input_num, sum))