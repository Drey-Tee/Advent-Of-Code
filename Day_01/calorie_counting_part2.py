data = open("input.txt").read()

cal_sums = []
sums = 0
for i in data.split("\n"):
    if len(i) == 0:
        cal_sums.append(sums)
        sums = 0
    else:
        sums += int(i)

cal_sums.append(sums)
cal_sums.sort()
print(cal_sums[-1] + cal_sums[-2] + cal_sums[-3])