import tkinter as tk

##blank에 들어있는 것들을 쌓기
    # 좌측에는 작성한 내용들, 우측에는 버튼
    # 버튼은 누르면 비밀번호 입력 창이 나옴 -> 맞으면 삭제, 틀리면 재입력
    
def post_type(blank, middle_frm):
    #초기화부터 진행
    for widget in middle_frm.winfo_children:
        widget.destroy()
        
    # blank에 있는 내용들을 꺼내서 보여주는 로직   
    for i in range(len(blank)):
        #내용들 꺼내기
        contents = blank[i]["내용"]
        
        #버튼와 제목들을 담을 공간 형성
        frm = tk.Frame(middle_frm)
        frm.pack(side="top")
        
        #제목을 띄울 공간 형성
        label = tk.Label(frm, text=contents)
        label.grid(row=0, column=0)

        #삭제 버튼
        btn = tk.Button(frm, text="X")
        btn.grid(row=0, column=1) 