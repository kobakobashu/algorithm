n = int(input())
s = input()

ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            cur = 0
            for num in s:
                if cur == 0 and int(num) == i:
                    cur = 1
                elif cur == 1 and int(num) == j:
                    cur = 2
                elif cur == 2 and int(num) == k:
                    ans += 1
                    break

print(ans)