# 현제 월을 입력하세요
mot = int(input("월을 입력하세요 : "))
# 1월부터 12월 까지 있습니다
if mot >= 1 and mot <= 12 :
    # 만약 입력받은 점수가 1~3일떄
    if mot >= 3 and mot <= 5 :
        # 봄입니다 출력
        print("봄 입니다" .format(mot))
    elif mot >= 6 and mot <= 8 :
        # 여름입니다 출력
        print("여름 입니다" .format(mot))
    elif mot >= 9 and mot <= 11 :
        # 가을입니다 출력
        print("가을 입니다" .format(mot))
    # elif mot == 12 or mot == 2 or mot == 1 :
    else :
        # 겨울입니다 출력
        print("겨울 입니다" .format(mot))
# 아니면
else :
    print("해당 월은 없습니다.")