from ToyManager import ToyManager
from toyVOs import Toy, Bycicle, Drone, GameConsole

class ToyUI(object):
    __mgr = ToyManager()

    def __init__(self):
        while True:
            print('=== Toy Menu ===')
            print('1. 장난감 등록')
            print('2. 장난감 검색')
            print('3. 장난감 삭제')
            print('4. 장난감 가격검색')
            print('5. 장난감 정보출력')
            print('9. 종료')
            selector = int(input('선택: '))

            if selector == 1:
                ToyUI.add()
            elif selector == 2:
                ToyUI.search()
            elif selector == 3:
                ToyUI.delete()
            elif selector == 4:
                ToyUI.search_price()
            elif selector == 5:
                ToyUI.info_show()
            elif selector == 9:
                print("종료")
                break
            else:
                print('[에러] 잘못 입력했습니다.')

    @classmethod
    def add(cls):
        vo = None

        print("=== 장난감 등록메뉴===")
        print("1. 자전거")
        print("2. 드론")
        print("3. 게임콘솔")
        selector = int(input("[ 장난감 선택 ]"))

        product_num = str(input("고유번호: "))

        if cls.__mgr.search(product_num) == None:
            name = str(input("이름: "))
            price = int(input("가격: "))

            if selector == 1:
                type = int(input("자전거 종류(1.도로용 2.산악용): "))
                vo = Bycicle()
                vo.product_num = product_num
                vo.name = name
                vo.price = price
                vo.type = type
            elif selector == 2:
                wings = int(input("날개수: "))
                vo = Drone(product_num, name, price, wings)
            elif selector == 3:
                portable = True
                portable = int(input("휴대성(1. 휴대가능, 2. 휴대불가): "))
                vo = GameConsole(product_num, name, price, portable)

        if vo == None:
            print("[에러] 잘못 입력하셨습니다.")
        else:
            print("[알림] 저장성공" if cls.__mgr.add_product(vo) else "[에러] 저장실패")

    @classmethod
    def search(cls):
        product_num = str(input("고유번호: "))

        searched_product = cls.__mgr.search(product_num)

        print(searched_product.show() if searched_product != None else "[에러] 검색결과가 없습니다.")

    @classmethod
    def delete(cls):
        product_num = str(input("삭제할 번호: "))

        print("[알림] 삭제완료" if(cls.__mgr.delete(product_num)) else "[에러] 삭제할 제품이 없습니다.")

    @classmethod
    def search_price(cls):
        min_price = int(input("최소가격: "))
        max_price = int(input("최대가격: "))

        searched_results = cls.__mgr.search_price(min_price, max_price)

        for vo in searched_results:
            print(vo.show())

    @classmethod
    def info_show(cls):
        for vo in cls.__mgr.list:
            print(vo.show())