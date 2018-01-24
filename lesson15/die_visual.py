import pygal
from die import Die
import time

print(time.ctime())
# 抛一个色子
die = Die()
# 同时抛两个色子
die1 = Die(10)
numbers = []
for roll_num in range(100000):
    result = die.roll() + die1.roll()
    numbers.append(result)

frequencies =[]
for value in range(2,die.num_sides + die1.num_sides + 1):
    count = numbers.count(value)
    frequencies.append(count)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 100 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

print(time.ctime())