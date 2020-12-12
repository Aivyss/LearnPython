class Parent:
    word = ''

    def __init__(self, num1, num2, string):
        self.num1 = num1
        self.num2 = num2
        Parent.word = string

    @staticmethod
    def static_method():
        print("Static method")

    @classmethod
    def class_method(cls):  # cls의 첫 매개변수가 요구됨.
        print(cls.word+"Class method")

    def instance_method(self):  # self 첫 매개변수가 요구됨.
        print("Instance method: ", self.num1, self.num2)


class Child(Parent):
    def __init__(self, num1, num2, string):
        Parent.__init__(self, num1, num2, '자식클래스가 건드림: ')
        Child.word = string

i = Parent(1, 2, '상속 전: ')
j = Child(3, 4, '상속 뒤: ')

i.class_method()
j.class_method()

j.instance_method()