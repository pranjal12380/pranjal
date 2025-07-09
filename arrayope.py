from functools import reduce

numbers = [3, 1, 4, 1, 5, 9]

# Sum using lambda and reduce
sum_ = reduce(lambda acc, x: acc + x, numbers, 0)

# Reverse using lambda and reduce
reverse = reduce(lambda acc, x: [x] + acc, numbers, [])

# Max using lambda and reduce
max_ = reduce(lambda acc, x: x if x > acc else acc, numbers)

# Min using lambda and reduce
min_ = reduce(lambda acc, x: x if x < acc else acc, numbers)

print("Sum:", sum_)         # Sum: 23
print("Reverse:", reverse)  # Reverse: [9, 5, 1, 4, 1, 3]
print("Max:", max_)         # Max: 9
print("Min:", min_)         # Min: 1
