'''
파일 저장 명 : 8장_0531_1_최민호.py

작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 최민호
문제 : 8장 파일 입출력
'''

# ptext.txt 파일을 copytext.txtx 파일로 복사
source = input("원본 파일 입력 : ")
target = input("복사본 파일 입력 : ")

with open(source, "r") as f :
    texts = f.read()   # 파일의 모든 내용을 읽고 변수에 저장
    
with open(target, "w") as f :
    f.write(texts)     # texts 내용을 target에 쓰기(출력)
    
print("{} 파일이 생성되었습니다. " .format(target))