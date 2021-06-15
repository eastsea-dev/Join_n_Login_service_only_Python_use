#오늘이 생일일 때 생일축하 메시지 코드
def hbdmsg(name, bd):
    from datetime import datetime
    today = str(datetime.today().month) + str(datetime.today().day)

    if len(today) == 3:
        today = '0' + today
    if today == bd[-5:-1]:
        print(name+"님", "생일 축하합니다!")

#로그인 절차 코드
def loginprocess():
    userid = input("ID:")
    userpw = input("PW:")

    infile = open("cusinfo.txt", 'r')
    lines = infile.readlines()
    item = 0
    for line in lines:
        item = line.split(",")
        if item[0] == userid:
            userpwcheck = item[1]
            if userpwcheck == userpw:
                print("로그인 성공")
                username = item[2]
                birthday = item[3]
                hbdmsg(username, birthday)
                break
            else:
                print("PW가 잘못되었습니다.")
                loginprocess()
                break
    if item[0] != userid:
        print("회원정보가 없습니다.")
        loginprocess()

#회원가입 코드
# !비밀번호 빈칸, 쉼표 입력시 오류 출력 필요
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

    if enternum == '1':
        loginprocess()
        break
    elif enternum == '2':
        joinprocess()
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
