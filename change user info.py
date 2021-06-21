#개인정보수정
#IDEA ok
#비밀번호 한 번 더 체크 ok
#바꿀 개인정보 선택 ok
#바꾸기 ok
#완료

def webfunction:
    print("1.개인정보수정\n2.미정")
    enternum = input("수행하실 업무를 선택해주세요.:")

    if enternum == '1':
        checkpw = input("비밀번호를 입력해주세요:")
        if checkpw == userpwcheck:
            selectnum = input("변경하실 항목을 선택해주세요.\n1.비밀번호 2.이름 3.생년월일\n:")
            if selectnum == '1':
                changepw = input("새 비밀번호를 입력해주세요:")
                changepwcheck = input("한 번 더 입력해주세요:")
                while changepw != changepwcheck:
                    print("입력하신 비밀번호가 다릅니다. 다시 입력해주세요.")
                    changepw = input("비밀번호를 입력해주세요:")
                    changepwcheck = input("비밀번호를 한 번 더 입력해주세요:")
                print("비밀번호가 변경되었습니다.")
                #비밀번호 변경 프로세스

            elif selectnum =='2':
                changename = input("개명하신 이름을 입력해주세요:")
                print("계정의 이름이", changename, "으로 변경되었습니다.")
                #이름 변경 프로세스
            elif selectnum == '3':

                changebirth = input("변경할 생년월일을 입력해주세요:")
                print("계정의 생년월일 정보가", changebirth, "으로 변경되었습니다.")
                #생년월일 변경 프로세스
