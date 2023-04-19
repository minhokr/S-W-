#1. 나이를 입력하세요.
age = int(input("나이를 입려하세요. : "))
#2. 키를 입력하세요.
cm = int(input("키를 입력하세요. : "))
#3. 나이가 8세 이상이면
if age >= 8 :
    #키가 120이상 이면
    if cm >= 120 :
        #고속 롤로코스터 입장가능.
        print("고속 롤로코스터 입장가능")
    #아니면
    else :
        print("저속 롤로코스터 입장가능")
#아니면
else :
    print("입장할 수 없습니다.")


age = int(input("나이를 입려하세요. : "))
cm = int(input("키를 입력하세요. : "))
if age >= 8 and cm >= 120 :
    if age >= 8 and cm >= 120 :
        print("고속 롤로코스터 입장가능")
    elif age >= 8 and cm < 120 :
        print("저속 롤로코스터 입장가능")
else :
    print("입장하실수 없습니다")