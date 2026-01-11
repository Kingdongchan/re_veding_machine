import tkinter as tk
from tkinter import messagebox

import CRUD.post as pst
#게시판 창에서 저장을 눌렀을 때 뜨는 창 -> 비밀번호를 써야하는 창
# entry 1개(비밀번호 입력창), 저장버튼
#만약에 입력창에 아무 것도 안 써있다면 내용를 써달라는 경고문이 나타났으면 좋겠음
def entry_type (entry, blank, middle_frm):
    
    #입력창에 내용을 변수에 할당
    e= entry.get()
    
    if e == "":
        messagebox.showwarning("경고", "내용을 입력해주세요.")
    else:   
            root = tk.Toplevel()
            root.title("비밀번호 설정")
            root.geometry("200x100")

            #열과 행에다가 가중치를 줌( 입력창와 저장버튼 중간 이동)
            root.grid_columnconfigure(0, weight=1)
            root.grid_rowconfigure(0, weight=1)

            #입력창
            ety = tk.Entry(root)
            ety.grid(row=0, column=0, sticky="e")
                    
            #버튼
            btn = tk.Button(root, text="확인", command=lambda: save_pwd())
            btn.grid(row=0, column=1, sticky="w")

            #배열에 추가하고 알림창 삭제
            def save_pwd ():
                pwd =ety.get()
                # 만약 아무것도 안쓴다면 저장이 안되게 만들어야함
                if pwd == "":
                    return False
                
                else:
                    blank.append({"내용":e, "password":pwd, "manager_pwd":"1111"})
                    ety.delete(0, tk.END)
                    entry.delete(0, tk.END)
                    root.destroy()
                    
                    pst.post_type(blank, middle_frm)
            
            root.mainloop()