import tkinter as tk
# 돈이 얼마나 들어왔는지에 대한 입력창이 필요함 
## 결제 버튼이 존재함
    #새로운 창에서는 100, 500, 1000, 5000, 10000, 카드, 입력완료이 있어야함
    #현금은 넣을때마다 입력창에 돈이 늘어나야함
    #카드의 경우에는 True or False로 형성
    
root = tk.Tk()
#가중치 형성
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

#입력창 형성
ent = tk.Entry(root, width=25)
ent.grid(row=0, column=0)

#'결제 방식 선택' 버튼 형성
bnt = tk.Button(root, text="결제 방법 선택")
bnt.grid(row=1, column=0, sticky="e")

root.mainloop()