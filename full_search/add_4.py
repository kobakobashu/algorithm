n, m = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(n)]
max_score = 0
ans = 0

for i in range(m - 1):
    for j in range(i + 1, m):
        sum_score = 0
        for k in range(n):
            max_score = max(num_list[k][i], num_list[k][j])
            sum_score += max_score
        ans = max(ans, sum_score)
print(ans)