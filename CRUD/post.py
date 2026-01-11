import tkinter as tk
from tkinter import messagebox
##blank에 들어있는 것들을 쌓기
    # 좌측에는 작성한 내용들, 우측에는 버튼
    # 버튼은 누르면 비밀번호 입력 창이 나옴 -> 맞으면 삭제, 틀리면 재입력
    
def post_type(blank, middle_frm):
    #초기화부터 진행
    for widget in middle_frm.winfo_children():
        widget.destroy()
        
    # blank에 있는 내용들을 꺼내서 보여주는 로직   
    for i in range(len(blank)):
        #내용들 꺼내기
        contents = blank[i]["내용"]
        
        #버튼와 제목들을 담을 공간 형성
        frm = tk.Frame(middle_frm)
        frm.pack(side="top", fill="both")
        
        #제목을 띄울 공간 형성
        label = tk.Label(frm, text=contents)
        label.pack(side="left")

        #삭제 버튼
        btn = tk.Button(frm, text="X", command=lambda idx= i:del_post(blank, idx, middle_frm))
        btn.pack(side="right") 
        
#삭제하는 로직 형성
def del_post(blank, i, middle_frm):
    #비밀번호 물어보는 새로운 창을 형성
    del_window = tk.Toplevel()
    del_window.title("비밀번호를 입력하세요.")
    
    #비밀번호 입력창
    pwd_entry = tk.Entry(del_window)
    pwd_entry.pack(side="left", expand=True)
    
    #'확인' 버튼
    pwd_btn = tk.Button(del_window, text="확인", command=lambda: del_content())
    pwd_btn.pack(side="left", expand=True)
    
    def del_content():
        #입력된 비밀번호를 변수로 입력
        password_input= pwd_entry.get()
        
        #만약 관리자 비밀번호나 사용자가 작성한 비밀번호가 같다면 삭제 
        # 아니라면 다시 입력하다록 알림창 새성
        if password_input == blank[i]["password"] or password_input == blank[i]["manager_pwd"]:
            del blank[i]    
            # 삭제 후 새로고침이 필요함
            post_type(blank, middle_frm)
            del_window.destroy()
        else:
            messagebox.showwarning("오류", "비밀번호가 틀렸습니다. 다시 입력해주세요.")
            
    del_window.mainloop()