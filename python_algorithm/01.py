N = input()
integer_N = int(N)
min_sum = 0

M = N
while int(M) >= integer_N - (len(N)-1) * 9:
    num_sum = 0
    for num in M:
        num_sum += int(num)
    if int(M) + num_sum == integer_N:
        min_sum = int(M)

    M = str(int(M)-1)

print(min_sum)
