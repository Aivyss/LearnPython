class Cal(object):
    # constructor
    def __init__(self, num1, num2):
        self.member1 = num1
        self.member2 = num2
        # 멤버변수를 따로 정의 안해도 되네..?
        # self는 생성한 인스턴트 그 자체, 굳이 self라는 이름을 쓰지 않아도 되지만 관습

    def add(self):
        return self.member1 + self.member2

    def subtract(self):
        return self.member1 - self.member2


# 클래스와 클래스 사이에는 두칸을 띄어쓰기
# 상속
class CalExtend(Cal):
    def times(self):
        return self.member1 * self.member2

    def div(self):
        return self.member1 / self.member2


# 둘다 멤버변수가 직접변수로 되어 있어서 출력은 된다. 자바에서 public 멤버변수와 같음
c1 = Cal(20, 30)  # instance 1
print(c1.member1, c1.member2, c1.add(), c1.subtract())

c2 = Cal(10, 10)  # instance 2
print(c2.member1, c2.member2, c2.add(), c2.subtract())

# 상속 예제
c3 = CalExtend(50, 10)
container = [c3.add(), c3.subtract(), c3.times, c3.div()]
print(container)
