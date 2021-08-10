s = input()
acgt_list = "ACGT"

cur_len_acgt = 0
max_len_acgt = 0

for alph in s:
    if alph in acgt_list:
        cur_len_acgt += 1
        max_len_acgt = max(cur_len_acgt, max_len_acgt)
    else:
        cur_len_acgt = 0

print(max_len_acgt)