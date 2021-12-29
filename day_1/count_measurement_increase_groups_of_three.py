with open('input.txt') as f:
    measurements = f.readlines()

window_sums = []
for i, _m in enumerate(measurements):
    if (i+2) > (len(measurements) - 1):
        print(f"Dropping window from index {i} as not enough measurements left to build window of 3")
    window_slice = measurements[i:i+3]
    window_slice = [int(i) for i in window_slice]
    window_sums.append(sum(window_slice))

# Lifted from challenge 1
increase_count = 0
for i, m in enumerate(window_sums):
    if i == 0:
        continue
    if int(m) > int(window_sums[i-1]):
        increase_count += 1

print(f"There were {increase_count} increases")
