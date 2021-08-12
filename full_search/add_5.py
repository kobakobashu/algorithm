a, b, c, x, y = map(int, input().split())

# exam1
if x <= y:
    exam1 = x * 2 * c + (y - x) * b
else:
    exam1 = y * 2 * c + (x - y) * a

# exam2
exam2 = a * x + b * y

# exam3
exam3 = max(x, y) * 2 * c

print(min(exam1, exam2, exam3))