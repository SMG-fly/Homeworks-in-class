print("안녕하세요 ABC 온라인 쇼핑몰입니다.")
grade = int(input("회원등급을 입력해주세요[Gold(1)/Silver(2)/Bronze(3)]: "))

if (grade == 1) or (grade == 2) or (grade == 3) :

    charge = int(input("구매 금액을 입력해주세요: "))

    if grade == 1 :
        if charge >= 20000 :
            print("고객님은 Gold 회원이시기 때문에 20% 할인이 적용되어", (charge*(8/10)), "원을 결제하시면 됩니다. 감사합니다." )
        elif charge > 0 :
            print("고객님은 Gold 회원이시기 때문에 10% 할인이 적용되어", (charge*(9/10)), "원을 결제하시면 됩니다. 감사합니다.")
        else :
            print("금액 정보가 올바르지 않습니다. 프로그램을 다시 시작해주세요.")

    elif grade == 2 :
        if charge >= 15000 :
            print("고객님은 Silver 회원이시기 때문에 10% 할인이 적용되어", (charge*(9/10)), "원을 결제하시면 됩니다. 감사합니다." )
        elif charge > 0 :
            print("고객님은 Silver 회원이시기 때문에 5% 할인이 적용되어", (charge*(95/100)), "원을 결제하시면 됩니다. 감사합니다.")
        else :
            print("금액 정보가 올바르지 않습니다. 프로그램을 다시 시작해주세요.")

    elif grade == 3 :
        if charge >= 10000 :
            print("고객님은 Bronze 회원이시기 때문에 5% 할인이 적용되어", (charge*(95/100)), "원을 결제하시면 됩니다. 감사합니다." )
        elif charge > 0 :
            print("할인 정보가 없습니다. 감사합니다.")
        else :
            print("금액 정보가 올바르지 않습니다. 프로그램을 다시 시작해주세요.")
 
else :
    print("등급 정보가 올바르지 않습니다. 프로그램을 다시 시작해주세요.")