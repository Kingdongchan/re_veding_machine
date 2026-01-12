import tkinter as tk

import keypad as kp
##배출구
# 배출구는 동전 반환 배출구와 상품 배출구가 존재함
# 배출되면 클릭으로 가져갔다는 것으로 간주함
# 클릭하면 버튼이 사라져야 함

for i in kp.repayment:
    prd = i["product"]
    coin = i["return"]

root = tk.Tk()
root.geometry("300x300")
##틀 만들기 - 동전, 상품
#1. 동전 틀
coin_frm = tk.Frame(root, width=50, height=50, bg="lightgray")
coin_frm.pack(side="left", expand=True)

#2. 상품 툴
coin_frm = tk.Frame(root, width=80, height=80, bg="lightgray")
coin_frm.pack(side="left", expand=True)

root.mainloop()