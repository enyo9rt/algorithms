a = int(input())
b = input()
if len(str(a)) != 3 and len(b) != 3:
    exit()
print(int(b[2]) * a)
print(int(b[1]) * a)
print(int(b[0]) * a)
print(int(b) * a)
