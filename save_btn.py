import tkinter as tk
#게시판 창에서 저장을 눌렀을 때 뜨는 창 -> 비밀번호를 써야하는 창
# entry 1개(비밀번호 입력창), 저장버튼

root = tk.Tk()
root.title("비밀번호 설정")
root.geometry("200x100")

#열과 행에다가 가중치를 줌( 입력창와 저장버튼 중간 이동)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

#입력창
entry = tk.Entry(root)
entry.grid(row=1, column=0, sticky="e")
#버튼
btn = tk.Button(root, text="확인")
btn.grid(row=1, column=1, sticky="w")

root.mainloop()