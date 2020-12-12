class ToyManager(object):
    def __init__(self):
        self.__list = []

    def add_product(self, toy):
        flag = False

        if toy != None:
            self.list.append(toy)
            flag = True
        else :
            flag = False

        return flag

    def search(self, product_num):
        result = None

        for vo in self.list:
            if product_num == vo.product_num:
                result = vo
                break

        return result

    def delete(self, product_num):
        flag = False
        searched_product = self.search(product_num)

        if searched_product !=None:
            self.list.remove(searched_product)
            flag = True

        return flag

    def search_price(self, min_price, max_price):
        container = []

        for vo in self.list:
            if vo.price >= min_price and vo.price <= max_price:
                container.append(vo)

        return container

    @property
    def list(self):
        return self.__list




