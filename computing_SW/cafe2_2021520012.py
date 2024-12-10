print("안녕하세요 AI카페입니다. ", end = '')
menu = []
while True :
    choose = int(input("무엇을 도와드릴까요? 메뉴추가(1)/메뉴출력(2)/나가기(3)/메뉴삭제(4): "))
    
    if choose == 1 :
        name = input("메뉴이름을 알려주세요: ")
        price = int(input("메뉴가격을 알려주세요: "))
        menu_one = [price, name]
        menu.append(menu_one)

    elif choose == 2:
        menu.sort() 
        for x, y in menu: 
            print(y, ":", x, "원")


    elif choose == 3: 
        print("감사합니다!!")
        break    

    elif choose == 4:
        rm_name = input("삭제할 메뉴 이름을 알려주세요: ")
        for menu_one in menu:
            if menu_one[1] == rm_name:
                menu.remove(menu_one)

    else:
        print("잘못된 입력입니다.")
                         
