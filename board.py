import tkinter as tk

import save_btn as sbtn
### CURD 게시판 만들기
    ## 프레임 3개 필요함 -> 맨위에 관리자가 쓰는 라벨, 쌓이는 메모장, 입력창
    #1. 관리자가 쓰는 라벨 -> "원하시는 상품을 써주세요." 라는문구가 나와야함
    #2. 쌓이는 메모장 -> 입력창에서 게시 누르면 위에서 부터 차곡차곡 쌓여야 함
            # 우측에 버튼이 하나 있고 버튼을 누르면 '비밀번호를 입렿하세요' 새로운 메지창 출력
            # 비밀번호가 맞다면 삭제, 틀리다면 '다시 입력해주세요' 출력
            # 관리자 비밀번호가 있고 관리자 비밀번호는 모든 것을 지울 수 있음
    #3. 입력창 -> 입력할 수 있는 공간, 우측에 '게시' 버튼이 존재함
    
#게시판을 쓰면 들어갈 배열을 형성
blank = []

root = tk.Tk()
root.geometry("250x200")

###프레임 3개를 형성###

##1. 관리자가 쓰는 라벨 
top_frm = tk.Frame(root, width=250, bg="white")
top_frm.pack(side="top", fill="y")

#"원하시는 상품을 써주십시오." 라벨 형성
manager_label = tk.Label(top_frm, text="원하시는 상품을 써주십시오.")
manager_label.pack()

##2. 쌓이는 메모장
middle_frm = tk.Frame(root, width=250, bg="red")
middle_frm.pack(side="top", fill="y", expand=True)


#3. 엽력창
bottom_frm = tk.Frame(root, width=250, bg="white")
bottom_frm.pack(side="top", fill="y")

##blank에 들어있는 것들을 쌓기
    # 좌측에는 작성한 내용들, 우측에는 버튼
    # 버튼은 누르면 비밀번호 입력 창이 나옴 -> 맞으면 삭제, 틀리면 재입력
    
    
#입력창(entry)형성 1줄 -> 왼쪽
entry = tk.Entry(bottom_frm)
entry.grid(row=0, column=0, sticky="e")

#게시 버튼 -> 오른쪽 -> 버튼 클릭시 비밀번호를 쓰는 새로운 안내창이 나와야함
btn = tk.Button(bottom_frm, text="게시", width=1, height=1, command=lambda: sbtn.save(entry, blank))
btn.grid(row=0, column=1, sticky="w")


root.mainloop()