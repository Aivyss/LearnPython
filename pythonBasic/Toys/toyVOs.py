class Toy(object):
    def __init__(self):
        self.__product_num = ''
        self.__name = ''
        self.__price = 0

    def __init__(self, product_num, name, price):
        self.__product_num = product_num
        self.__name = name
        self.__price = price

    def show(self):
        return {"고유번호: ": self.__product_num, "이름: ": self.__name, "가격: ": self.__price}

    @property
    def product_num(self):
        return self.__product_num

    @product_num.setter
    def product_num(self, product_num):
        self.__product_num = product_num

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class Bycicle(Toy):
    def __init__(self, product_num, name, price, type):
        Toy.__init__(product_num, name, price)

    def __init__(self):
        self.__type = ''

        if type == 1:
            self.__type = '도로용'
        elif type == 2:
            self.__type = '산악용'

    # 메소드 오버라이드
    def show(self):
        dictionary = super().show()
        dictionary["타입: "] = self.type

        return dictionary

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        if type==1:
            self.__type = '도로용'
        elif type==2:
            self.__type = '산악용'


class Drone(Toy):
    def __init__(self):
        self.__wings = 0

    def __init__(self, product_num, name, price, wings):
        super().__init__(product_num, name, price)
        self.__wings = wings

    # 메소드 오버라이드
    def show(self):
        dictionary = super().show()
        dictionary["날개수: "] = self.wings

        return dictionary

    @property
    def wings(self):
        return self.__wings

    @wings.setter
    def wings(self, wings):
        self.__wings = wings


class GameConsole(Toy):
    def __init__(self):
        self.__portable = False

    def __init__(self, product_num, name, price, portable):
        super().__init__(product_num, name, price)

        if portable == 1 :
            self.__portable = "Yes"
        else :
            self.__portable = "No"



    #메소드 오버라이드
    def show(self):
        dictionary = super().show()
        dictionary["휴대용: "] = self.portable

        return dictionary

    @property
    def portable(self):
        return self.__portable

    @portable.setter
    def portable(self, portable):
        if portable == 1:
            self.portable = "Yes"
        elif portable == 2:
            self.portable = "No"

