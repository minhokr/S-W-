'''
파일 저장 명 : 8장_0530_1_최민호.py

작성일 : 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 최민호
문제 : 8장 파일 입출력
'''

# open() 함수로 파일 읽기 - read() 메소드
f = open("test.txt", "r")    # 파일 오픈(읽기)

test = f.read()
print(test)

f.close()    # 파일 종료