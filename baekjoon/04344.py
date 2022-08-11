import sys

case = int(sys.stdin.readline())
students = []
data = [0]*case
result = []

for i in range(case):
    score = 0
    data[i] = list(map(int, sys.stdin.readline().split()))
    students.append(data[i][0])
    average = (sum(data[i]) - data[i][0]) / data[i][0]
    for j in range(students[i]):
        if data[i][j+1] > average:
            score += 1
    result.append(round(score * 100 / students[i], 3))
for i in range(case):
    print("{:.3f}%".format(result[i]))
