n = int(input())

for i in range(1, n+1):
    plus = list(map(int, str(i)))
    ans = i + sum(plus)

    if(ans == n):
        print(i)
        break

    if(n == i):
        print(0)
