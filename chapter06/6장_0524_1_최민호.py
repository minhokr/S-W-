# 튜플 생성
tuple1 = ()   # 빈 튜플
tuple2 = ('a',)   # 원소가 하나여도 쉼표는 필수!!!
tuple3 = ('a', 'b', 'c')

color = ('white', 'blue', 'green', 'white', 'red')
print("color 내용 : ", color)
print("color의 길이 : ", len(color))
print("white의 개수 : ", color.count('white'))    #화이트의 개수
print('blue 의 위치 : ', color.index("blue"))     #블루의 위치(주소)

# 실습 예제 6-7
# 2개의 튜플을 하나의 리스트로 만들기
fruit = ('사과', '복숭아', '수박', '딸기', '망고')
price = (2000, 4500, 8000, 12000, 5500)

# 결과 [사과, 2000, 복숭아, 4500 ---]
fp_list= []   # 2개의 튜플 내용이 저장 될 리스트 생성.
fp_tuple = ()   # 2개의 튜플 내용이 저장 될 튜플 생성.

for i in range(len(fruit)) :
    fp_list.append(fruit[i])
    fp_list.append(price[i])
    # fp_tuple.append(fruit[i])   # 튜플은 변경이 안됨. 추가 안됨.
    
print("가격 목록 : ", price)
print("과일의 가격 리스트 : ", fp_list)