'''
작성일 : 2023년 4월 12일
학과 : 컴퓨터공학부
학번 : 202395032
이름 : 최민호
설명 : 두 개의 숫자를 입력받아 도 숫자가 모두 짝수이면 두 숫자가 모두 짝수입니다.
        모두 홀수이면 두 숫자가 모두 홀수입니다를 출력합니다 그렇지 않으면
        짝수와홀수가 섞여있습니다를 출력하는 프로그램을 만드시오
'''
#1. 정수를 입력 받는다.
num1 = int(input("정수를 입력하세요"))
num2 = int(input("정수를 입력하세요"))
#2. 만약 입력받은 정수가 0보다 크면
#   1)"00은 짝수입니다"
if num1%2==0 and  num2%2==0 :
    print("둘다 짝수입니다.")
#2. 만약 입력받은 정수가 0보다 적으면
#   1)"00은 홀수입니다"
elif num1%2==1 and  num2%2==1 :
    print("둘다 홀수입니다.")
#3. 아니면
#    1)홀수와 짝수가 섞여있습니다.
else :
    print("홀수와 짝수가 섞여있습니다.")