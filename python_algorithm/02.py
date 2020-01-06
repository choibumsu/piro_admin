N = int(input())
cal_num = [0, 0, 1, 1]

for num in range(4, N+1):
    temp = 9999999
    if num % 3 == 0:
        temp = min(temp, cal_num[int(num/3)] + 1)
    if num % 2 == 0:
        temp = min(temp, cal_num[int(num/2)] + 1)
    temp = min(temp, cal_num[num - 1] + 1)
    cal_num.append(temp)
print(cal_num[N])
