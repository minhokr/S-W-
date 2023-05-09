#1 점수를 soc에 각각저장한다

sub = 1
total = 0
while sub <= 5 :
    soc = int(input(str(sub) + " 번째 성적 입력"))
    
    if(soc >= 0 and soc <= 100) :
        total = total + soc
        print(sub,"번째 성적 : ", soc)
        sub = sub + 1
    else :
        print("유요한 성적이 아닙니다.")
        continue
    print("총점 :", total)
    
    print("평균 :" , total / 5)