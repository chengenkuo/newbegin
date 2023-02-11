from sys import exit
def login():
    chance=3
    acc="ABC123"   
    pswd="abc123"
    chance=3
    for x in range(chance):
        chance-=1
        account=input("請輸入帳號")
        password=input("請輸入密碼")
        if(account==acc)and(password==pswd):
            print("登入成功")
            break
        else:
            if(chance==0):
                print("帳號已鎖定,請找管理員")
                exit()
            else:
                print("帳號密碼錯誤還剩",str(chance),"次機會,帳號將鎖定")
def leave():
    print("歡迎下次再度使用!")
    exit()            




def shooting_cal():
    print("投籃命中率計算機")
    attempt=int(input("投了幾球?"))
    made=int(input("投進幾球?"))
    percentage=made/attempt*100
    if(percentage<=100)and (percentage>=90):
        print(int(percentage),"% 你是神射手!")
    elif(percentage<=80)and(percentage>=50):
        print(int(percentage),"% 你很準喔!")
    else:
        print(int(percentage),"% 再練練你可以的!")


def bike():
    print("自行車租借系統")
    total=15
    print("目前可租借數量:",total)
    choose=input("請輸入 1.歸還 2.租借")


    while(choose=="2"):
        user=eval(input("請輸入欲租借數量:"))
        if(user<total):
            total-=user
            print("租借成功,尚有",str(total),"台可借")
   
    
        else:
            print("租借失敗,僅有"+str(total)+"台可借")

    else:
        user_back=eval(input("請輸入欲歸還數量:"))
        total+=user_back
        print("歸還成功,目前可租借數量:",str(total),"台")




def size():
    print("尺寸建議")
    gender=input("請輸入您的性別:1.男 2.女")
    hei=int(input("請輸入您的身高: cm"))
    wei=int(input("請輸入您的體重: kg"))

    if(gender=="1"):
        if(hei>=189)or(wei>=83):
            print("請選男生XL號")
        elif(181<=hei<=188) or (76<=wei<=82):
            print("請選男生L號")
        elif(173<=hei<=180)or (63<=wei<=75):
            print("請選男生M號")
        elif(165<=hei<=172)or (55<=wei<=62):
            print("請選男生S號")
  
    if(gender=="2"):
        if(hei>=171)or(wei>=61):
            print("請選女生XL號")
        elif(166<=hei<=170)or(56<=wei<=60):
            print("請選女生L號")            
        elif(161<=hei<=165)or(51<=wei<=55):
            print("請選女生M號") 
        elif(152<=hei<=160)or(45<=wei<=50):
            print("請選女生S號") 
def home_page():
    choose=input("請選擇以下要執行的程式:\n1.投籃命中率計算\n2.自行車租借\n3.尺寸建議\n0.離開程式")
    if(choose=="0"):
        leave()
    elif(choose=="1"):
        shooting_cal()
    elif(choose=="2"):
        bike()
    elif(choose=="3"):
        size()
    else:
        print("輸入錯誤,請重新輸入:")
        
    home_page()
print("您好!請登入程式")
login()

print("歡迎登入")
home_page()
        
    
    
    
