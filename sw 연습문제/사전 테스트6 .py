#설명 : 컴퓨터, 영어 과목의 점수를 입력 받아 두 과목 중 한 과목의 성적이 95점 이상이거나,
        # 두 과목의 합이 170점 이상이면 "합격입니다"를 출력하고,
        # 아니면 "불합격입니다."를 출력하는 프로그램을 작성하시
        
#1. 변수를 저장한다.
com = int(input("점수를 입력하세요. : "))    
eng = int(input("점수를 입력하세요. : "))    

#2. 한 과목의 점수가 95점 이상이거나 두 과목의 합이 170점 이상이면 합격을 출력한다
if com >= 95 or eng >=95 or com+eng >= 170 :
    print("합격입니다.")
    
#3. 아니면
else : 
    print("불합격입니다.")