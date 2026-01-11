import tkinter as tk
from tkinter import messagebox

import product as pd
import board 
import payment
import keypad
## 프레임 먼저 설정
# 메인프레인와 보조 프레임들이 필요함
# 메인 프레임:보조브레임 = 7:3 비율
# 보조 프레임에는 상단부터 -> CRUD:결제:키패드:배출구 = 3:1:3:1 비율
    # 1. CRUD입력창 프레임(원하는   음식을 적기 위한 입력창)
    # 2. 결제 프레임 - 금액을 얼마나 넣었는지에 대한 공간, 결제 할 방법 선택하기
    # 3. 키패드 프레임 - 캐리드는 위에는 어떤 번호를 썼는지 확인할 수 있는 입력창이 필요함 (입력창은 = "disabled")
    # 4. 배출구 프레임 - 동전 반환 공간와 상품을 받을 공간을 구별해야함

root = tk.Tk()
root.title("자판기")
# 메인 틀 형성
root.geometry("800x600")


# 메인 프레인 형성
main_frm = tk.Frame(root, width=550, bg = "lightgray")
main_frm.pack(side="left", fill="both", expand=True)

#메인프레임 상품 목록들을 출력하는 함수
pd.main_prd(main_frm)

#사이드 프레임 형성
side_frm = tk.Frame(root, width=250, bg = "white")
side_frm .pack(side="left", fill  = "y", expand=True)

side_frm.pack_propagate(False)

#######사이드 프레임 나누기#######

#1. 사이드 프레임 -CURD 프레임 
board_frm = tk.Frame(side_frm, width=250, height=250, bg="white")
board_frm.pack(side="top")

#창이 늘어나지 않고 고정되도록 하는 명령어 추가
board_frm.pack_propagate(False)

    # CRUD 입력창 로직 
board.crud_board(board_frm)

#2. 사이드 프레임 - 결제 프레임 
payment_frm = tk.Frame(side_frm, width=250, bg="white")
payment_frm.pack(side="top", fill="y", expand=True)
    #결제 로직
payment.user_payment(payment_frm)

#3. 사이드 프레임 - 키패드 프래임
keypad_frm = tk.Frame(side_frm, width=250, bg="white")
keypad_frm.pack(side="top", fill="y", expand=True)

    #키패드 로직
keypad.key_number(keypad_frm)

#4. 사이드 프레임 - 배출구 프레임
output_frm = tk.Frame(side_frm, width=250, bg="white")
output_frm.pack(side="top", fill="y", expand=True)


root.mainloop()
