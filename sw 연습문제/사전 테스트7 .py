#1. 정수를 입력한다.
num = int(input("정수를 입력하세요. : "))

#2. 입력 받은 정수가 4자리이상 경우
if num >= 1000 or num <= -1000 :
    print("네 자리이상 정수입니다.")
elif num >= 100 or num <= -100 :
    print("세 자리 정수입니다.")
elif num >= 10 or num <= -10 :
    print("두 자리 정수입니다.")
else :
    print("한 자리 정수입니다.")