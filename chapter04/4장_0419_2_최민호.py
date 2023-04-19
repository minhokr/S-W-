#1. 숫자를 num으로 저장
#2. 연산자를 cal로 저장
num1 = int(input("첫번쨰 수를 입력하세요. : "))
cal = (input("연산자를 입력하세요. : "))
num2 = int(input("두번쨰 수를 입력하세요. : "))

#3. 만약 연산자가 + 라면
if cal == '+' :
    print("{} + {} = {} " .format(num1, num2, num1+num2))
#4. 만약 연산자가 - 라면
elif cal == '-' :
    print("{} - {} = {}" .format(num1, num2, num1-num2))
#5. 만약 연산자가 / 라면
elif cal == '/' :
    print("{} / {} = {}" .format(num1, num2, num1/num2))
#6. 만약 연산자가 * 하면
elif cal == '*' :
    print("{} * {} = {}" .format(num1, num2, num1*num2))
#7.아니면
else :
    print("연산자를 잘못입력 하셨습니다.")
    