import tkinter as tk

##메인 플레임 - 상품 진열
    # 20개의 프레임을 형성(4x5 형식)
    # 20개의 상품을 배치 -> 리스트안 딕셔너리 형태 -> {번호, 상품이름, 가격, 재고}
    
def main_prd (main_frm):
    #20개의 상품 만들기
    prd = [
        {"num":1 ,"product": "코카콜라" ,"price":1400 ,"stock":5 },
        {"num":2 ,"product": "펩시콜라" ,"price":1200 ,"stock":5 },
        {"num":3 ,"product": "미에로화이바","price":900 ,"stock":5 },
        {"num":4 ,"product": "망고쥬스","price":1000 ,"stock":5 },    
        {"num":5 ,"product": "갈아만든 배","price":1300 ,"stock":5 },
        {"num":6 ,"product": "몬스터에너지","price":2200 ,"stock":5 },
        {"num":7 ,"product": "코코팜","price":1300 ,"stock":5 },
        {"num":8 ,"product": "포카리스웨트","price":1300 ,"stock":5 }, 
        {"num":9 ,"product": "초코송이","price":1300 ,"stock":5 },
        {"num":10 ,"product": "오레오","price":1600 ,"stock":5 },
        {"num":11,"product": "화이트하임","price":1500 ,"stock":5 },
        {"num":12 ,"product": "예감","price":1600 ,"stock":5 },
        {"num":13 ,"product": "초코쿠키","price":1300 ,"stock":5 },
        {"num":14 ,"product": "다이제 씬","price":1500 ,"stock":5 },
        {"num":15 ,"product": "에너지 초코바","price":1300 ,"stock":5 },
        {"num":16 ,"product": "빠다코코낫","price":1600 ,"stock":5 }, 
        {"num":17 ,"product": "신라면","price":1300 ,"stock":5 },
        {"num":18 ,"product": "참깨라면","price":1300 ,"stock":5 },
        {"num":19 ,"product": "육개장 사발면","price":1300 ,"stock":5 },
        {"num":20 ,"product": "불닭볶음면","price":1500 ,"stock":5 }
    ]



    #상품 숫자와 상품명만 출력
    for i in range(len(prd)):
        number = prd[i]["num"]
        product = prd[i]["product"]
        prd_price = prd[i]["price"] 
        num_prd = f"{number}. {product} {prd_price}원"
        
        # 20개의 제품 틀을 만들기 
        r = i//4
        c = i%4
        
        #상품을 담을 프레임 형성 
        prd_frm = tk.Frame(main_frm, width=130, height=100, bg="white")
        prd_frm.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
        
        #
        prd_frm.grid_propagate(False)
        
        #높이와 넓이를 만들기 위한 가중치 형성
        prd_frm.grid_columnconfigure(0, weight=1)
        prd_frm.grid_rowconfigure(0, weight=1)
        
        #프레임 안에 상품명을 담을 라벨 생성(하단에 배치)
        prd_label = tk.Label(prd_frm, text=num_prd)
        prd_label.grid(row=0, column=0, sticky="s")

    ##공간을 모두 사용하기 위해 가중치 주는 명령어 사용
    #열에 대한 가중치
    for z in range(4):
        main_frm.grid_columnconfigure(z, weight=1)

    #행에 대한 가중치
    for q in range(5):
        main_frm.grid_rowconfigure(q, weight=1)
        
        

    