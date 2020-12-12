# Author : Aivyss
str1, str2 = input().split()
str1 = str(str1)
str2 = str(str2)
list1 = []
list2 = []

# "A" --> 65
for one in str1:
    list1.append(ord(one))

for one in str2:
    list2.append(ord(one))

list1.reverse()
list2.reverse()

sum = 0
for index, one in enumerate(list1):
    sum += (one-65)*(5**index)

for index, one in enumerate(list2):
    sum += (one-65)*(5**index)

index = 0
while True:
    if int(sum / 5**index) != 0:
        index +=1
    else:
        index -= 1
        break

result = ""
while index >= 0:
    result += chr(int(sum / 5**index)+65)
    sum = sum % 5**index
    index -= 1

print(result)