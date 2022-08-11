list = []
for i in range(10000):
    list.append(i + 1)
for i in range(10000):
    d = (i + 1) + ((i + 1) // 10000) + ((i + 1) // 1000) + ((i + 1) // 100 % 10) + ((i + 1) // 10 % 10) + ((i + 1) % 10)
    if list.count(d) > 0:
        list.remove(d)
for i in range(len(list)):
    print(list[i])
