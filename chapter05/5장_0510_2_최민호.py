print("for 반복문으로 구구단을 출력하세요.")

for dan in range(2,10) :
    print("{} 단".format(dan))
    for num in range(1, 10) :
        if (dan*num) %2 == 0 :
            print("{} X {} = {}" .format(dan,num,dan*num))
            
    
    
dan = 2

while dan <= 9 :
    print("{} 단".format(dan))
    num = 1
    while num <= 9 :
        if (dan*num) %2 == 0 :
            print("{} X {} = {}" .format(dan,num,dan*num))
        num = num + 1      
    dan = dan + 1
    
    
    
            