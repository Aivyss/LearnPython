import itertools
from math import fabs

n, k = input().split()
n = int(n)
k = int(k)

items = list(range(1, 2 * n + 1))
case = list(itertools.combinations(items, n))
a_person = case[:int(len(case)/2)]
b_person = case[int(len(case)/2):]
b_person.reverse()

count = 0
for index, a_case in enumerate(a_person):
    sum = 0
    b_case = b_person[index]

    for i in range(0, n):
        sum += fabs(a_case[i] - b_case[i])

        if sum > k:
            break

    if sum <= k:
        count += 2

print(count)