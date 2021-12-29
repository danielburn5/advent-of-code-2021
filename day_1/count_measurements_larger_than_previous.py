with open('input.txt') as f:
    measurements = f.readlines()

increase_count = 0
for i, m in enumerate(measurements):
    if i == 0:
        continue
    if int(m) > int(measurements[i-1]):
        increase_count += 1

print(f"There were {increase_count} increases")
