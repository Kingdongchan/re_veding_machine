
import keypad as kp
import tkinter as tk
##배출구
# 배출구는 동전 반환 배출구와 상품 배출구가 존재함
# 배출되면 클릭으로 가져갔다는 것으로 간주함
# 클릭하면 버튼이 사라져야 함
def output_prd (output_frm):
    
    ##틀 만들기 - 동전, 상품
    #1. 동전 틀
    coin_frm = tk.Frame(output_frm, width=50, height=50, bg="lightgray")
    coin_frm.pack(side="left", expand=True)

    coin_btn = tk.Button(coin_frm, text=str(kp.repayment["return_coin"]), command=lambda:destroy_bnt(coin_btn))
    coin_btn.pack(expand=True)

    #2. 상품 툴
    prd_frm = tk.Frame(output_frm, width=80, height=80, bg="lightgray")
    prd_frm.pack(side="left", expand=True)

    prd_btn = tk.Button(prd_frm, text=kp.repayment["product"], command=lambda:destroy_bnt(prd_btn))
    prd_btn.pack(expand=True)
 
 #클릭하면 파괴되는 함수
def destroy_bnt (event):
    event.destroy()