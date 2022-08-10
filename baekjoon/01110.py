import sys

N = int(sys.stdin.readline())
first = N
count = 0
while True:
    count += 1
    N = 10 * (N % 10) + (N // 10 + N % 10) % 10
    if N == first:
        print(count)
        break
