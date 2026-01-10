import tkinter as tk
from tkinter import messagebox

## 프레임 먼저 설정
# 메인프레인와 보조 프레임들이 필요함
# 메인 프레임:보조브레임 = 7:3 
# 보조 프레임에는 상단부터
    # 1. CRUD입력창 프레임(원하는 음식을 적기 위한 입력창)
    # 2. 결제 프레임 - 금액을 얼마나 넣었는지에 대한 공간, 결제 할 방법 선택하기
    # 3. 키패드 프레임 - 캐리드는 위에는 어떤 번호를 썼는지 확인할 수 있는 입력창이 필요함 (입력창은 = "disabled")
    # 4. 배출구 프레임 - 동전 반환 공간와 상품을 받을 공간을 구별해야함

root = tk.Tk()
root.title("자판기")
# 메인 틀 형성
root.geometry("800x600")


root.mainloop()
