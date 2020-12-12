# Author: Aivyss
# Create date: 2020 11 25

def reverse_str(string):
    """  문자열을 뒤집는 함수 
        매개변수: 문자열
    """
    result = ''

    for one in string[::-1]:
        result += one

    return result


def empty_1d_list(type, size):
    """  원하는 사이즈의 1차원의 리스트를 생성 
        매개변수: 타입(문자열기재), 리스트크기
    """
    container = []

    if type == "int":
        for i in range(0, size):
            container.append(0)
    elif type == "str":
        for i in range(0, size):
            container.append("")

    return container


def empty_2d_list(type, row_size, col_size):
    """  원하는 사이즈의 2차원의 리스트를 생성 
        매개변수: 타입(문자열기재), 행의 크기, 열의 크기
    """
    result = []
    unit = 0

    if type == "int":
        unit = 0
    elif type == "str":
        unit = ''

    for j in range(0, row_size):
        container = []

        for i in range(0, col_size):
            container.append(unit)

        result.append(container)

    return result


def change_notation(notation, number):
    """ 진법변환 함수. 낮은 자리수부터 배치
    """
    result = []

    power = 0
    while True:
        if int(number / notation ** power) != 0:
            power += 1
        else:
            power -= 1
            break

    while power >= 0:
        temp = int(number / notation ** power)
        result.append(temp)
        number -= temp * notation ** power

        power -= 1

    result.reverse()

    return result
