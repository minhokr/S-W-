# 첫번쨰 과목
score1 = int(input("첫번쨰 점수를 입력하세요. : "))
# 두번쨰 과목
score2 = int(input("두번쨰 점수를 입력하세요. : "))
# 총합
total = score1+score2

# 모두 75점 이상
if score1>=75 and score2>=75:
# 만약 두 과목의 점수가 180점 이상이면
    if total >=180 :
        print("{}점은 최우수 학생입니다." .format(total))
        # 만약 두 과목의 점수가 160점 이상이면
    elif total >=160 :
        print("{}점은 우수 학생입니다." .format(total))
        # 만약 두 과목의 점수가 150점 이상이면
    else:
        print("{}점은 보통 학생입니다." .format(total))
# 아니면
else :
    print("분발합시다.")