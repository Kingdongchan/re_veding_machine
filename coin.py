import tkinter as tk

root = tk.Tk()
root.title("결정 방식 선택")
root.geometry("350x100")

coin_type = [
    "100", "500", "1000", "5000", "10000", "카드"
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
    
    btn = tk.Button(root, text=c, width=2, height=2)
    btn.grid(row=1, column=i)

root.mainloop()