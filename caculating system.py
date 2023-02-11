def checkout():
    #先提供各品項價格
    coke=25
    milktea=20
    blacktea=30
    gum=10
    meat=15
    egg=5
    coke_choose=1
    milktea_choose=2
    blacktea_choose=3
    gum_choose="A"
    meat_choose="B"
    egg_choose="C"
    total=0      
    from sys import exit
    while True:
        #利用while迴圈輸入不同品項時輸入購買數量並計算總價
        choose=input("選擇購買的品項:1.可樂 2.奶茶 3.紅茶 4.結帳")
        if (choose=="1"):
            coke_amnt=input("輸入購買數量:")
            total+=coke*int(coke_amnt)
            print("總共",total,"元")
        elif (choose=="2"):
            milktea_amnt=input("輸入購買數量:")
            total+=milktea*int(milktea_amnt)
            print("總共",total,"元")
        elif (choose=="3"):
            blacktea_amnt=input("輸入購買數量:")
            total+=blacktea*int(blacktea_amnt)
            print("總共",total,"元")
        elif(choose=="4"): #選到選項4時詢問要加購商品
            #利用while迴圈輸入不同加購品項及數量
            while True:
                add_choice=input("是否加購以下商品A.口香糖 B.肉乾 C.茶葉蛋 D.謝謝不用")
                if (add_choice=="A"):
                    gum_amnt=input("輸入購買金額:")
                    total+=gum*int(gum_amnt)
                    print("一共是",total,"元")
                elif (add_choice=="B"):
                    meat_amnt=input("輸入購買數量:")
                    total+=meat*int(meat_amnt)
                    print("一共是",total,"元")
                elif (add_choice=="C"):
                    egg_amnt=input("輸入購買數量:")
                    total+=egg*int(egg_amnt)
                    print("一共是",total,"元")
                else:
                    #若不選擇加購,則選擇D,計算總價跳出迴圈
                    print("總共是",total,"元")
                    exit()

checkout()


    
