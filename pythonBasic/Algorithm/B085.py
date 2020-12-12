from math import fabs

# Author: Aivyss 20201124

position = int(input())
index = 0

solution_1 = 0
index = fabs(position)

if position >=0:
    solution_1 = int(index*(2*index-1))
else:
    solution_1 = int(index*(2*index-1) + 2*index)


solution_2 = 0
for p in range(0, 15):
    if fabs(position) <= 2**(p):
        index = p
        break

# left side
sum = 0
for x in range (0, p+1):
    if x > 0:
        sum = sum + 2**(x-1)
    sum = sum + 3*(2**x)

if position >= 0:
    solution_2 = int(sum + position-3*(2**index))
else:
    solution_2 = int(sum - 2**index - position)

print(solution_1, end=" ")
print(solution_2)