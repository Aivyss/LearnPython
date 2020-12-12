# Author: Aivyss 20201124

move = int(input())
text = str(input())

# 26
index = 0
result = ''
for one in text:
    if (index + 1) % 2 == 0:
        if ord(one) + move <= 90:
            one = chr(ord(one) + move)
        else:
            one = chr(ord(one) + move - 26)
    else:
        if ord(one) - move >= 65:
            one = chr(ord(one) - move)
        else:
            one = chr(ord(one) - move + 26)

    result = result + one
    index = index + 1

print(result)
