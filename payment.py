import tkinter as tk

import payment_.coin as coin
import product
# 돈이 얼마나 들어왔는지에 대한 입력창이 필요함 
## 결제 버튼이 존재함
    #새로운 창에서는 100, 500, 1000, 5000, 10000, 카드, 입력완료이 있어야함
    #현금은 넣을때마다 입력창에 돈이 늘어나야함
    #카드의 경우에는 True or False로 형성
def user_payment(payment_frm):
    #가중치 형성
    payment_frm.grid_rowconfigure(0, weight=1)
    payment_frm.grid_rowconfigure(1, weight=1)

    #입력창 형성
    insert_ent = tk.Entry(payment_frm, width=25, state="disabled")
    insert_ent.grid(row=0, column=0)

    #'결제 방식 선택' 버튼 형성
    bnt = tk.Button(payment_frm, text="결제 방법 선택", command=lambda: coin.coin_window(insert_ent))
    bnt.grid(row=1, column=0, sticky="e")

