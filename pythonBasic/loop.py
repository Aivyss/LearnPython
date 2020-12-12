# list() 함수로 리스트화
# range()는 iterable한 함수. 순차적으로 꺼냄.
container = list(range(0, 10))
print(container)

# 자바의 가장 기본이되는 for문과 같은 기능을 수행
# 하지만 다른 부분도 존재함
for x in range(0, 10):
    print(x)
    x = x * 10  # 자바와 다른 부분, for문이 끝나지 않는다.
    print(x)

print("=============")

container2 = list(range(0, 10))
container3 = [25, True, "String", {"Key1": 11, "key2": False, "key3": "String"}, ('남자', '여자'), None]

# 자바의 for-each 처럼 사용할 수도 있다.
for x in container2:
    print(x)
for x in container3:
    print(x)

# 배열에 아주 편하게 한줄로 집어넣을 수도 있다.
container4 = [x for x in range(10, 20)]
print(container4)

a = 10
b = 10

# 삼항연산자1 하지만 정수 a와 b가 같은 경우에 대해서 제대로 처리하지 못함 --> 쓰지마
c = a == b and a - b or a + b
print(c)  # 결과가 30이 나오는 정신나간 결과가 나온다. "(조건1 and 조건2) or 조건3" 처럼 처리하기 때문.

# 삼항연산자2
c = a - b if a == b else a + b
print(c)  # 아주 바람직하게 나온다. "참결과 if 조건 else 거짓결과" 구조를 띤다.
