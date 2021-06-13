#로그인 절차 코드
def loginprocess():
    userid = input("ID:")
    userpw = input("PW:")

    infile = open("cusinfo.txt", 'r')
    while userid !=
    #if 첫번째 chr 틀리면 다음줄 체크
    #elif 첫번째 chr 맞으면 다음글자 체크

    while userpw !=
#if 첫번째 chr 틀리면 다음줄 체크
#elif 첫번째 chr 맞으면 다음글자 체크

#for문 idea: 공백까지 체크, 일치하지 않으면 한줄 내려서 체크 맞는게 있다면 브레이크
#그리고 그 줄 첫 공백부터 끝 공백까지 userpw와 비교 일치하면 로그인 일치하지 않으면 비번 틀렸다고 출력

#회원가입 절차 코드
# !비밀번호 빈칸, 쉼표 입력시 오류 출력 필요(
def joinprocess():
    id = input("사용하실 ID를 입력해주세요:")#나중에 중복확인까지 추가해보기
    pw = input("비밀번호를 입력해주세요:")
    pwre = input("비밀번호를 한 번 더 입력해주세요:")

    while pw != pwre:
        print("입력하신 비밀번호가 다릅니다. 다시 입력해주세요.")
        pw = input("비밀번호를 입력해주세요:")
        pwre = input("비밀번호를 한 번 더 입력해주세요:")

    urname = input("이름을 입력해주세요:")
    birthdate = input("생년월일을 입력해주세요:")
    print("회원가입 완료!")

    infile = open("cusinfo.txt", 'a')
    cusinfo = [id, ",", pw, ",", urname, ",", birthdate, "\n"]

    infile.writelines(cusinfo)
    infile.close()

    loginprocess()

#main 화면 코드
enternum = 0
while enternum != '1' or '2':
    print("join & login service using only python\n1.login\n2.join\n")
    enternum = input("please enter the number you want:")
    #switch문으로도 해보기
    if enternum == '1':
        loginprocess()
        break
    elif enternum == '2':
        joinprocess()
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
