n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]

x_list = []
y_list = []

for num in num_list:
    x_list.append(num[0])
    y_list.append(num[1])

x_list.sort()
y_list.sort()

in_x = x_list[n // 2]
out_y = y_list[n // 2]

ans = 0
for num in num_list:
    ans += abs(num[0] - in_x) + (num[1] - num[0]) + abs(num[1] - out_y)

print(ans)