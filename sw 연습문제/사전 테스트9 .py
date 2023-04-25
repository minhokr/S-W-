# 설명 : 아이디와 패스워드를 입력 받아 로그인 인증 결과를출력하는 프로그램을 작성하시오.
id = "horing"
psw = "minho789"
id_s = input("아이디를 입력하세요. : ")
psw_s = input("패스워드를 입력하세요. : ")
#2. 패스워드와 아이디가 맞는지 확인
if id != id_s and psw != psw_s :
    print("아이디 패스워드 둘다 틀렸습니다.")
    
#3. 아이디만 틀렸을 경우
elif id != id_s :
    print("아이디가 틀렸습니다")

#4. 패스워드가 틀렸을 경우
elif psw != psw_s :
    print("패스워드가 틀렸습니다")
    
else :
    print("로그인 되었습니다")    
