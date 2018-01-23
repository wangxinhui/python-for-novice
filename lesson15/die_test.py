from die import Die

d = Die()
numbers = []
for roll_num in range(100):
    result = d.roll()
    numbers.append(result)
print(numbers)

counts = []
for value in range(1,d.num_sides+1):
    count = numbers.count(value)
    counts.append(count)
print(counts)