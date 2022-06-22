from random import randint

def generate_num(): #랜덤한숫자만드는 함수
    num=[]
    i=0
    newnum=0
    while i<3:
        newnum=randint(1,9)
        if newnum not in num:
            num.append(newnum)
            i+=1
    print("랜덤한 숫자 선택")
    return num

def selectnum():
    print("예측한 숫자 입력")
    i=0
    newinputnum=[]
    while i<3:
        inputnum=int(input("{}번째 숫자 입력하기: ".format(i+1)))
        if inputnum > 9 and inputnum<1: #이상한 숫자 입력한 경우
            print("잘못된 숫자 입력입니다")
            continue
        if inputnum in newinputnum: #중복
            print("중복된 숫자 입력입니다")
        else:
            newinputnum.append(inputnum)
            i +=1
    return newinputnum

def score(input,answer):
    strike_count=0
    ball_count=0
    i=0

    while i<3:
        if input[i]==answer[i]:
            strike_count+=1
            i+=1
        elif input[i] in answer:
            ball_count+=1
            i+=1
        else:
            i+=1
    return strike_count, ball_count

#
rightanswer=generate_num()
tries=0

while(1):
    guess=selectnum()
    strike,ball=score(guess,rightanswer)
    print("{}S {}B ".format(strike, ball))

    if strike ==3:
        print("아웃")
        tries+=1
        break
    else:
        tries+=1
print("정답 {}번 만에 맞췄습니다.".format(tries))

