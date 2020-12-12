# Author:  Aivyss

# get test case
n, k = input().split()
n = int(n)
k = int(k)

# define variables
input_list = []
output_list = []

# input data
for x in range(0, n):
    input_sub_list = []
    temp = input().split()

    for y in temp:
        input_sub_list.append(int(y))

    input_list.append(input_sub_list)

# create empty list
for x in range(0, int(n/k)):
    temp = []

    for y in range (0, int(n/k)):
        temp.append(0)

    output_list.append(temp)

# fill output list
for i in range(0, n):
    for j in range(0, n):
         output_list[int(i/k)][int(j/k)] += input_list[i][j]

# Average process & print
for i in range(0, int(n/k)):
    for j in range(0, int(n/k)):
        output_list[i][j] = int(output_list[i][j]/k**2)
        if j != int(n/k)-1:
            print(str(output_list[i][j]), end=" ")
        else:
            print(str(output_list[i][j]))



