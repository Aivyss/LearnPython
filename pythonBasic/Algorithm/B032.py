# Author: Aivyss

def upper_side(str_list):
    power = 0
    summ = 0

    for one_line in str_list[0][::-1]:
        if one_line == "|":
            summ = summ + 5 * 10 ** power

        power += 1

    return summ


def under_side(str_list):
    summ = 0

    index2 = 0
    for one_line in str_list[3:]:
        index1 = 0

        for char in one_line[::-1]:
            if char == "|":
                summ = summ + index2 * 10 ** index1

            index1 += 1
        index2 += 1

    return summ


w = int(input())
str_list_1 = []
str_list_2 = []
result = []

for x in range(0, 8):
    str_list_1.append(str(input()))

index = 0
for x in range(0, 8):
    str_list_2.append(str(input()))

    if index == 2:
        divider = ''

        for y in range(0, w):
            divider += "="

        result.append(divider)
    else:
        result.append('')

    index += 1

summation = 0
summation += upper_side(str_list_1)
summation += upper_side(str_list_2)
summation += under_side(str_list_1)
summation += under_side(str_list_2)

while w - 1 >= 0:
    one = int(summation / 10 ** (w - 1))
    summation = summation % 10 ** (w - 1)
    w -= 1

    if one >= 5:
        result[0] += "|"
        result[1] += "*"
        one -= 5
    else:
        result[0] += "*"
        result[1] += "|"

    if one == 4:
        result[3] += "*"
        result[4] += "*"
        result[5] += "*"
        result[6] += "*"
        result[7] += "|"
    elif one == 3:
        result[3] += "*"
        result[4] += "*"
        result[5] += "*"
        result[6] += "|"
        result[7] += "*"
    elif one == 2:
        result[3] += "*"
        result[4] += "*"
        result[5] += "|"
        result[6] += "*"
        result[7] += "*"
    elif one == 1:
        result[3] += "*"
        result[4] += "|"
        result[5] += "*"
        result[6] += "*"
        result[7] += "*"
    else:
        result[3] += "|"
        result[4] += "*"
        result[5] += "*"
        result[6] += "*"
        result[7] += "*"

for line in result:
    print(line)
