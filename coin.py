import tkinter as tk

def coin_window (insert_ent):
    
    root = tk.Toplevel()
    root.title("결제 방식 선택")
    
    coin_type = [
        100, 500, 1000, 5000, 10000, "카드"
    ]

    # 가중치 주기
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    #입력창 -> 사용자가 건들 수 없게끔 만들어야 함
    ent = tk.Entry(root, state="normal")
    ent.grid(row=0, column=0, columnspan=6)

    init= "0"
    ent.insert(0, init)
    ent.config(state="disabled")
        
    #배열 속 버튼들을 만드는 반복문 생성
    for i in range(len(coin_type)):
        
        c = coin_type[i]
        
        btn = tk.Button(root, text=c, width=2, height=2, command=lambda idx=c : payment_type(idx))
        btn.grid(row=1, column=i)
        
    #투입완료 버튼 
    ok_bnt = tk.Button(root, text="투입 완료", command=lambda:destory_window(insert_ent))
    ok_bnt.grid(row=2, column=5)

    #만약 카드를 누른다면 True와 Faluse로 구별함 (신용카드로 가정하고 만듬)
    #나머지 버튼을 누르면 버튼 속에 있는 숫자들을 계속해서 더해줌
    def payment_type(num):
        
        count = ent.get()
        
        ent.config(state="normal")
        
        if num == "카드":
            ent.insert(0, "True")
            ent.config(state="disabled")
            destory_window()
            
        else:
            # get() 명령어는 배열의 숫자도 문자열로 알기 떄문에 int명령어를 써줘서 숫자로 바꿔주는 역할을 해야됨
            new_count = int(count) + num
        
            ent.delete(0, tk.END)
            ent.insert(0, str(new_count))
            ent.config(state="disabled")

    #창을 없애는 로직 형성
    def destory_window(insert_ent):
        result = ent.get()
        
        insert_ent.insert(0, result)
        root.destroy()
        
