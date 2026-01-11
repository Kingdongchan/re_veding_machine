import tkinter as tk

root = tk.Tk()
root.title("결정 방식 선택")
root.geometry("350x100")

coin_type = [
    100, 500, 1000, 5000, 10000, "카드"
]

# 가중치 주기
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

#입력창 -> 사용자가 건들 수 없게끔 만들어야 함
ent = tk.Entry(root, state="disabled")
ent.grid(row=0, column=0, columnspan=6)

#배열 속 버튼들을 만드는 반복문 생성
for i in range(len(coin_type)):
    
    c = coin_type[i]
    
    btn = tk.Button(root, text=c, width=2, height=2, command=lambda idx=c : payment_type(idx))
    btn.grid(row=1, column=i)
    
#투입완료 버튼 
ok_bnt = tk.Button(root, text="투입 완료", command=lambda:destory_window())
ok_bnt.grid(row=2, column=5)

#만약 카드를 누른다면 True와 Faluse로 구별함 (신용카드로 가정하고 만듬)
#나머지 버튼을 누르면 버튼 속에 있는 숫자들을 계속해서 더해줌
def payment_type(num):
    
    count = ent.get()
    
    if num == "카드":
        ent.config(state="normal")
        ent.insert(0, "True")
        ent.config(state="disabled")
        destory_window()
        
    else:
        count = count + num
        
        ent.config(state="normal")
        ent.insert(0, f"{count}")
        ent.config(state="disabled")
        
def destory_window():
    root.destroy()
    
root.mainloop()