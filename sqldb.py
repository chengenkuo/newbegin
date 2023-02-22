import pymysql
conn=pymysql.connect(host="Localhost",user="David",passwd="kuodavid1021",db="my_david_db",charset="utf8")
cur=conn.cursor()
#連線至mysql中my_david_db的資料庫
def myindex():
    print("登入管理者系統")
    print("---------------------")
    print("1.登入會員")
    print("2.註冊會員")
    print("3.結束程式")
def index_2():
    print("選擇欲執行的項目")
    print("1.查詢所有員工資料")
    print("11.查詢單一員工資料")
    print("2.修改員工資料")
    print("3.刪除員工資料")
    print("4.離開")
    
    
def interface():
    while True:
        print("選擇欲執行的項目")
        print("1.查詢所有員工資料")
        print("11.查詢單一員工資料")
        print("2.修改員工資料")
        print("3.刪除員工資料")
        print("4.離開")
        move=input("選擇要執行的項目")
        if(move=="1"):
            print("查詢所有員工資料")
            search_info_all()
        elif(move=="11"):
            print("查詢單一員工資烙")
            search_info_one()
        elif(move=="2"):
            print("修改員工資料")
            edit_info()
        elif(move=="3"):
            print("刪除員工資料")
            del_acc()
        else:
           break
    
def mymenu():
    while True:
        myindex()
        num=int(input("請輸入欲執行的項目"))
        print()
        
        if num==1:
            print("登入")
            login()
        elif num==2:
            print("註冊會員")
            insert_info()
        elif num==3:
            print("結束程式")
            break

def login():
    while True:
        useracc=input("請輸入帳號:")
        if useracc=="":
            print("不允許為空值")
            break
        sql_1="SELECT stf_name,stf_acc,stf_pass FROM staff_info WHERE stf_acc='"+useracc+"'AND stf_del=0"
        cur.execute(sql_1)
        staff_acc=cur.fetchone()
        
        if(staff_acc==None):
            print("{}帳號不存在".format(useracc))
            continue
        userpswd=staff_acc[2]
        mypswd=input("請輸入密碼")
        
        if(mypswd==""):
            print("不允許為空值")
            break
        if(mypswd!=userpswd):
            print("密碼錯誤")
        else:
            print("登入成功")
            interface()
            break
def search_info_all():
   
    sql="SELECT stf_pk,stf_name,stf_acc,stf_pass,stf_level,stf_del FROM staff_info WHERE stf_del=0"
    cur.execute(sql)
    staff_data=cur.fetchall()
    print(staff_data)

def search_info_one():
    choose=input("輸入欲搜尋的欄位1.姓名2.帳號")
    if (choose=="1"):
        name=input("請輸入欲搜尋的名字")
        sql_1="SELECT stf_name,stf_acc,stf_pass FROM staff_info WHERE stf_name='"+name+"'AND stf_del='0'"
    else:
        search_acc=input("輸入欲查詢的帳號")
        sql_1="SELECT stf_name,stf_acc,stf_pass FROM staff_info WHERE stf_acc='"+search_acc+"'AND stf_del='0'"
    cur.execute(sql_1)
    data=cur.fetchone()
    print(data)
        
def insert_info():
    while True:
        name=input("請輸入姓名")
        if(name==""):
            print("姓名不能為空值")
            continue
        useracc=input("請輸入帳號")
        if(useracc==""):
            print("帳號不能為空值")
            continue
        sql_4="SELECT * FROM staff_info WHERE stf_acc='"+useracc+"'"
        cur.execute(sql_4)
        data=cur.fetchone()
        if not(data==None):
            print("{}帳號已存在".format(useracc))
            continue
        userpswd=input("請輸入密碼")
        sql_insert="INSERT INTO staff_info(stf_name,stf_acc,stf_pass)VALUES('"+name+"','"+useracc+"','"+userpswd+"')"
        cur.execute(sql_insert)
        conn.commit()
        print("已註冊成功".format(useracc))
        break

def edit_info():
    while True:
        updateacc=input("輸入要修改的帳號")
        sql_5="SELECT stf_name,stf_acc,stf_pass FROM staff_info WHERE stf_acc='"+updateacc+"'"
        cur.execute(sql_5)
        staff_data=cur.fetchone()
        if(staff_data==None):
            print("{}查無此帳號".format(updateacc))
            continue
        print(staff_data)
        
        newname=input("請輸入新的名字")
        sql_6="UPDATE staff_info SET stf_name='"+newname+"' WHERE stf_acc='"+updateacc+"'"
        cur.execute(sql_6)
        conn.commit
        
        cur.execute(sql_5)
        person=cur.fetchone()
        print(person)
        input("修改完成,請按任意鍵回主頁")
        break

def del_acc():
    while True:
        delacc=input("請輸入要刪除的帳號")
        sql_6="SELECT stf_name,stf_acc,stf_pass FROM staff_info WHERE stf_acc='"+delacc+"'"
        cur.execute(sql_6)
        data=cur.fetchone()
    
        if(data==None):
            print("{}此帳號不存在".format(delacc))
            continue
        print("你確定要刪除{}這個帳號".format(delacc))
        check=input("Y/N")
        if(check=="Y" or check=="y"):
            sql_7="DELETE staff_info FROM stf_acc='"+delacc+"'"
            cur.execute(sql_7)
            conn.commit
            input("刪除成功,請按任意鍵返回主頁")
            break

    
            
mymenu()
cur.close()
conn.close()
        
            
                
        
            
            
    