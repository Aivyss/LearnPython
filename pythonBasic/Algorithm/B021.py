test_case = int(input())

text_list = []
result_list = []
for text in range(0, test_case):
    text = str(input())
    text_list.append(text)

for text in text_list:
    if text[-1] == "s" or text[-1] == "o" or text[-1] == "x":
        text = text + "es"
    elif text[-2:] == "sh" or text[-2:] == "ch":
        text = text + "es"
    elif text[-1] == "f":
        text = text[:-1] + "ves"
    elif (text[-2:]) == "fe":
        text_fixed = ''

        for one in text[:-2]:
            text_fixed = text_fixed + one

        text = text_fixed + "ves"
    elif text[-2:] == "ay" or text[-2:] == "iy" or text[-2:] == "uy" or text[-2:] == "ey" or text[-2:] == "oy":
        text = text + "s"
    elif text[-1] == "y":
        text = text[:-1] + "ies"
    else:
        text = text + "s"

    result_list.append(text)

for text in result_list:
    print(text)
