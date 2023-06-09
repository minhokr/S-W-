'''
파일 저장 명 : 5장_0530_2_최민호.py

작성일 : 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 최민호
문제 : 7장 세트와 딕셔너리 
        01. 세트
        
예제 7-3
5명의 학번과 이름을 입력하여 딕셔너리에 저장한다.
키 : 학번   값 : 이름

학번을 입력 받아 해당 학생의 이름을 출력한다.
입력받은 학번이 없으면 "입력한 학생이 존재하지 않습니다.' 출력한다.
학번을 입력할 떄 사용자가 0을 입력하면 프로그램을 종료한다.
'''

#알고리즘
# 1. 빈 딕셔너리 만든다. - 학생 딕셔너리 만든다.
# 2. 5번 반복하면서
#       1) 학번을 입력 받는다.
#       2) 이름을 입력 받는다.
# 3. 저장된 학생 정보를 출력한다.
# 4. 학번에 0이 입력 될 때까지 반복한다. (무한반복하면서)
#       1) 검색할 학번을 입력반는다.
#       2) 만약에 학번이 0이면 
#           2-1) 프로그램 종료
#       3) 아니면
#           3-1) 만약에 학번이 있으면
#               a. 학생 정보 출력
#           3-2) 아니면
#               a. 입력한 학생이 없습니다.

student = {}
for i in range(5) :
    id = int(input(str(i+1) + "번째 학생 학번 입력 : "))
    name = input(str(i+1) + "번째 학생 이름 입력 : ")
    student[id] = name   # 해당 키에 값 저장
    
print("학생 명부 완성")
print(student)

while True :
    id = int(input(" 검색을 원하는 학생 학번 입력(종료:0) : "))
    if id == 0 :
        print("프로그램을 종료합니다.")
        break
    else :
        if id in student :
            print("== 검색한 학생 정보 == ")
            print("학번 : ", id, "이름 : ", student.get(id))
            print("학번 : ", id, "이름 : ", student[id])       # 위쪽과 결과는 똑같이 나온다.
        else :
            print("검색한 학생이 존재하지 않습니다.")