#1. 점수를 입력하세요
score = int(input("점수를 입력하세요 : "))
#2. 점수는 0이상이고 100이하이다.
if score >= 0 and score <= 100 :
#2. 만약 입력받은 정수가 90보다 크거나 같을떄 
#   1)" A학점입니다"
    if score >= 90 :
        print("{}점은 A학점입니다." .format(score))
#2. 만약 입력받은 정수가 80보다 크거나 같을떄 
#   1)" B학점입니다"
    elif score >= 80 :
        print("{}점은 B학점입니다." .format(score))
#2. 만약 입력받은 정수가 70보다 크거나 같을떄 
#   1)" C학점입니다"       
    elif score >= 70 :
        print("{}점은 C학점입니다." .format(score))
#2. 만약 입력받은 정수가 60보다 크거나 같을떄 
#   1)" D학점입니다"
    elif score >= 60 :
        print("{}점은 D학점입니다." .format(score))
# 아니면
# 1. 잘못입력된 점수를 입력하셨습니다.
else :
    print("{}점은 잘못된 점수입니다." .format(score))
