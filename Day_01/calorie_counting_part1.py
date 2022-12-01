data = open("input.txt").read()

current_max = 0
calories_sum = 0
for i in data.split("\n"):
    if len(i) == 0:
        calories_sum = 0
    else:
        calories_sum += int(i)

    current_max = max(current_max, calories_sum)

print(current_max)