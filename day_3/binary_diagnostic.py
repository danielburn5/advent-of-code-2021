from collections import defaultdict


def bit_counter(words):
    ret = defaultdict(list)
    for entry in words:
        for i, bit in enumerate(entry.strip()):
            ret[i].append(bit)
    return ret


with open('input.txt') as f:
    diagnostic_report = f.readlines()

# Part 1
bit_groupings = bit_counter(diagnostic_report)

gamma = ''
epsilon = ''

for key, value in bit_groupings.items():
    ones = value.count('1')
    zeros = value.count('0')

    gamma += ('1' if (ones > zeros) else '0')
    epsilon += ('1' if (ones < zeros) else '0')

print('--- PART ONE ---')
print(f"gamma={gamma}")
print(f"epsilon={epsilon}")
power_consumption = int(gamma, 2) * int(epsilon, 2)
print(f"The power consumption of the submarine is {power_consumption}")

# Part 2
def most_common(ones, zeroes):
    if ones >= zeroes:
        return '1'
    if zeroes > ones:
        return '0'


def least_common(ones, zeroes):
    if ones < zeroes:
        return '1'
    if zeroes <= ones:
        return '0'


def solve(comparison_func):
    candidates = diagnostic_report
    ret = None
    for key in range(0, 12):
        values_for_given_bit = bit_counter(candidates)[key]
        ones = values_for_given_bit.count('1')
        zeroes = values_for_given_bit.count('0')

        if len(candidates) > 1:
            candidates = [entry for entry in candidates if entry[key] == comparison_func(ones, zeroes)]

        if len(candidates) == 1:
            ret = candidates[0].strip()
            break
    return ret


oxygen_gen_rating = solve(most_common)
co2_scrubber_rating = solve(least_common)

print(f"oxygen_gen_rating={oxygen_gen_rating}")
print(f"co2_scrubber_rating={co2_scrubber_rating}")
life_support_rating = int(oxygen_gen_rating, 2) * int(co2_scrubber_rating, 2)
print(f"The life support rating is {life_support_rating}")
