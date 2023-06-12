
import random

student = {}

def lotto_numbers():                                                                   # 각기 다른 랜덤 로또 번호를 생성한다.
    numbers = random.sample(range(1, 46), 6)                                           # 1~46 번 까지 랜덤으로 6개의 번호 생성
    return numbers                                                                     # 숫자 반환

while True:
    student_id = input("학번을 입력하세요 (종료하려면 '0' 입력): ")                    # id에 학번을 저장한다.
    if student_id == '0':                                                              # 0을 입력하면 종료한다.
        break                                                                          # 멈춘다.
    
    student_name = input("이름을 입력하세요: ")                                        # name에 이름을 저장한다.
    student[student_id] = student_name, lotto_numbers()                                # id는 name,lottot  번호를 저장한다.
                    
while True:
    student_ward = input("검색을 원하는 학생 학번 입력 (종료: 0): ")                   # 검색하고 싶은 학번을 입력한다.
    if student_ward == 0:                                                              # 0을 입력하면 종료한다.                                                                      # 멈춘다.
        print("프로그램을 종료합니다.")
        break                                                                          # 멈춘다
    
    else:
        if student_ward in student:                                                    # 만약 검색한 학번이 저장되어 있으면
            print("== 검색한 학생 정보 ==")                                            # 정보출력
            print("학번 : ", student_ward,"이름 : ", student.get(student_ward))
        else: 
            print("검색한 학생이 존재하지 않습니다.")
            break
