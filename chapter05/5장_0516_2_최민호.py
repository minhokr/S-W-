'''
파일 저장 명 :  5장_0516_2_최민호.py
작성일 : 2023년 5월 16일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 사용자로부터 가장 좋아하는 월을 입력 받아 그 월에 해당되는 계절을 출력하는 프로그램을
       메뉴형태로 whlie 문을 사용하여 작성하시오.
[문제 분석]
변수 month
3,4,5 봄
6,7,8 여름
9,10,11 가을
12,1,2 겨울

변수 : sum, num, count
'''

while True :
    mot = int(input("월을 입력하세요 . : "))
    
    if mot == 3 or mot == 4 or mot == 5  :
        print ("봄입니다.")
    elif mot == 6 or mot == 7 or mot == 8 :
        print("여름입니다.")
    elif mot == 9 or mot == 10 or mot == 11  :
        print("가을 입니다.")
    elif mot == 12 or mot == 1 or mot == 2  :
        print("겨울 입니다.")
    elif mot == 0 :
        print("시스템이 종료됩니다.")
        break

    else :
        print("해당 월은 없습니다.")    