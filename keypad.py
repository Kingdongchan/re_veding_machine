import tkinter as tk

import payment as pm
## 키패드
    # 1,2,3,4,5,6,7,8,9,0 버튼 -> 누르면 가장 끝에 숫자가 붙어서 나와야함
    # 삭제버튼 -> 삭제하면 입력창에 있는 숫자들이 사라져야함
    # 결정버튼 -> 버튼을 누르면 상품이 나와야하며 입력창에는 
        # "결제를 해주셔서 감사합니다." 문구라 나와야함
        # 상품의 재고에서 -1를 해야함
    # 취소버튼 -> 번튼을 누르면 동전이 반환이 되어야함
        # "구매를 취소가 되었습니다."라는 문구가 나와야함
        # 만약에 반환할 돈이 없다면 "010-XXXX-XXXX로 연락주십시오" 라는 문구가 나와야함

return_coin = 5000


def key_number (keypad_frm):
    # 입력창 생성
    ent = tk.Entry(keypad_frm, state="disabled")
    ent.grid(row=0, column=0, columnspan=4, sticky="w")

    #키패듬 오양 -> 취소는 결정 옆에 두어야하기때문에 따로 뺴놓아야함
    key = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9,
        "삭제", 0, "결정"
    ]

    #반복문을 통해서 숫자 배열을 생성
    for index, i in enumerate(key):
        r = index//3+1
        c = index%3
        
        nmb_btn = tk.Button(keypad_frm, text=i, width=3, height=1, command= lambda idx=i:number_input(idx))
        nmb_btn.grid(row=r, column=c)
        
    #취소버튼 만들기
    cancel_btn = tk.Button(keypad_frm, text="취소", width=3, height=3, command=lambda:cancel_input())
    cancel_btn.grid(row=3, column=3, rowspan=2)

    #숫자버튼을 누르면 입력창 끝에 숫자들이 나와야함
    #삭제버튼을 누르면 입력창안에 있는 것들이 삭제가 되어야 함
    def number_input(num):
        global return_coin
        
        user_input = ent.get()
        
    #payment에서 정보 가져오기
        for j in pm.purchase_prd:
            prd_num = j["num"]
            pri = j["price"]
            pay_ = j["pay"]
            frm = j["frm"]
            typ = j["type"]
            stk = j["stock"]       
        
        if num == "삭제":
            ent.config(state="normal")
            ent.delete(0, tk.END)
            ent.config(state="disabled")
        
        
        #결정 버튼을 누르면 입력창에 "구매 감사합니다."라고 송출되어야 함.
        elif num == "결정":
            ## 만약에 결정을 누른다면 
            #   카드라면
                # 결정을 누른 뒤 프레임 색깔들 원상복귀
                # 재고가 하나 빠져야함
            #   현금이라면
                # 결정을 누른 뒤 프레임 색깔들 원상복귀 
                # 기존 돈에서 상품 가격만큼 돈 깎은 후 반환
                # 기계에 잔돈이 없다면 전화번호 노출
                # 기계에 잔돈이 있다면 '구매 감사합니다' 출력
            if typ == "카드":
                if ent in prd_num:
                    
                    stk = stk - 1
                
                    ent. config(state="normal")
                    ent.delete(0, tk.END)
                    ent.insert(tk.END, "구매 감사합니다.")
                    ent.config(state="disabled")
                    frm.config(bg="white")
                                       
            elif typ == "현금":
                if ent in prd_num:
                    stk = stk - 1
                    pay_ = int(pay_) - pri
                    
                    if pay_ > return_coin:
                        ent.config(state="normal")
                        ent.delete(0, tk.END)
                        ent.insert(0, "010-XXXX-XXX 연락주십시오.")
                        ent.config(state="disabled")
                    else:
                        return_coin = return_coin - pay_
                        frm.config(bg="white")
                        ent. config(state="normal")
                        ent.delete(0, tk.END)
                        ent.insert(tk.END, "구매 감사합니다.")
                        ent.config(state="disabled")
                        
                        
        else:
            ent. config(state="normal")
            ent.insert(tk.END, num)
            ent.config(state="disabled")
        
        #취소 버튼이 누르면 반환이 되면서 "취소되었습니다"라는 문구가 송출되어야 함.
        #만약에 넣은 돈이 반환할 돈보다 많다면 번호 노출
    def cancel_input():
        ent. config(state="normal")
        ent.delete(0, tk.END)
        ent.insert(0, "취소되었습니다.")
        ent.config(state="disabled")
        
