output_list = []
while True:
    num_list = list(map(int, input().split()))
    if num_list == [0, 0]:
        break
    output = 0
    for i in range(1, num_list[1]//3):
        for j in range(i + 1, num_list[1]//2):
            k = num_list[1] - i - j
            if j < k and k <= num_list[0]:
                output += 1
    output_list.append(output)

for ans in output_list:
    print(ans)