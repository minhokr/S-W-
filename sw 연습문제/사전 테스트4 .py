#1. 변수를 입력받는다.
mon = int(input("시급을 입력하세요. : "))
time = int(input("노동 시간을 입력하세요. : "))

#2. 수당 계산
total = mon * time

#3. 수당 총 계산 및 출력
print("시급은 {}원이고 노동시간은{}시간 입니다 총 수당은{}입니다." .format(mon, time, total))
print("시급은 {}원이고 노동시간은{}시간 입니다 총 수당은{}입니다." .format(mon, time, mon*time))