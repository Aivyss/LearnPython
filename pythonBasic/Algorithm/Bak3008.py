list = []
num_dot = int(input())

for x in range(0, num_dot):
    x_position, y_position = (input()).split()
    x_position = int(x_position)
    y_position = int(y_position)
    dot = [x_position, y_position]
    list.append(dot)

count = 0
rotate = 1
for index1 in range(0, len(list)-2):
    for index2 in range(index1+1, len(list)-1):
        for index3 in range(index2+1, len(list)):
            ax = list[index1][0]-list[index2][0]
            ay = list[index1][1]-list[index2][1]
            bx = list[index1][0]-list[index3][0]
            by = list[index1][1]-list[index3][1]
            cx = list[index3][0]-list[index2][0]
            cy = list[index3][1]-list[index2][1]

            aa = ax**2 + ay**2
            bb = bx**2 + by**2
            cc = cx**2 + cy**2

            if (aa + bb == cc) or (bb + cc == aa) or (cc + aa == bb):
                count += 1

print(count)
