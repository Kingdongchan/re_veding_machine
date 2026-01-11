import tkinter as tk

import payment_.coin as coin
import product as pd
# 돈이 얼마나 들어왔는지에 대한 입력창이 필요함 
## 결제 버튼이 존재함
    #새로운 창에서는 100, 500, 1000, 5000, 10000, 카드, 입력완료이 있어야함
    #현금은 넣을때마다 입력창에 돈이 늘어나야함
    #카드의 경우에는 True or False로 형성

#살수 있는 품목들 담기
purchase_prd = []

def user_payment(payment_frm):
    #가중치 형성
    payment_frm.grid_rowconfigure(0, weight=1)
    payment_frm.grid_rowconfigure(1, weight=1)

    #입력창 형성
    insert_ent = tk.Entry(payment_frm, width=25, state="disabled")
    insert_ent.grid(row=0, column=0)

    insert_ent.config(state="normal")
    insert_ent.insert(tk.END, "0")
    insert_ent.config(state="disabled")

    def chage_frm ():
        #product.py의 있는 배열 가져와서 비교한 뒤 프레임 색깔 변경
        current_coin = insert_ent.get()
    
        for i in pd.light_prd:
            frm = i["frm"]
            pri = i["price"]
            stk = i["stock"]
            num = i["num"]
            
            if current_coin == "True" and stk>0:
                frm.config(bg="red")
                purchase_prd.append({"type": "카드", "num": num, "price":pri, "frm":frm, "stock":stk})
            
            elif int(current_coin) >= pri and stk>0:
                frm.config(bg="red")
                purchase_prd.append({"type": "현금", "num": num, "price":pri, "pay":current_coin, "frm":frm, "stock": stk})
    
    #'결제 방식 선택' 버튼 형성
    bnt = tk.Button(payment_frm, text="결제 방법 선택", command=lambda: coin.coin_window(insert_ent, chage_frm))
    bnt.grid(row=1, column=0, sticky="e")
