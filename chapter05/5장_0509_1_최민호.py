#1 정수를 입력 받는다.
#2 1부터 입력 받은 수까지 반복하면서
#   2-1) 만약 수를 입력 받은 수로 나누어 나머지가 0이면
#  멈춘다.
#3 만약 입력 받은 정수가와 나누는 수가 같으면
#   3-1)소수 입니다.
#4 아니면
#   4-1) 소수가 아닙니다.

    
print("=====================================")
input_num = int(input("정수를 입력 하세요. : "))
for num in range(2,input_num+1) :
    if input_num % num == 0 :
        break
if input_num == num :
    print("{}은 소수입니다." .format(input_num))
else :
    print("{}은 소수가 아닙니다." .format(input_num))
