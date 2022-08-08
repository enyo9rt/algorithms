import sys

a, b = map(int, sys.stdin.readline().split())
if 1 <= (a and b) <= 10000:
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
