'''
파일 저장 명 :  3장_연습문제12_최민호.py
작성일 : 2023년 3월 29일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 연습문제 14.
       5과목의 점수를 입력 받아 총점과 평균을 구하는 프로그램을 작성하시오.
'''
score1 = int(input('국어점수의 값을 입력하시오. : '))

score2 = int(input('수학점수의 값을 입력하시오. : '))

score3 = int(input('사회점수의 값을 입력하시오. : '))

score4 = int(input('과학점수의 값을 입력하시오. : '))

score5 = int(input('영어점수의 값을 입력하시오. : '))

sum = (score1 + score2 + score3 + score4 + score5 ) / 5

print("국어 : ", score1, "수학 : ", score2, "사회 : ", score3 ,"과학 : ", score4,"영어 : ", score5)
print("평균변수는 ", sum, "입니다.")

print("국어 : {} 수학 : {} 사회 : {}" "영어 : {}" "과학 : {}".foramt(score1, score2, score3, score4, score5))
print(" 평균 총점은는 {:.2f}입니다." .format(sum))