n = int(input())
output = 0

for i in range(1, n + 1, 2):
    divisor_count = 0
    for div in range(1, i + 1):
        if i % div == 0:
            divisor_count += 1
    if divisor_count == 8:
        output += 1

print(output)