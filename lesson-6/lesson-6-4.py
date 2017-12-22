# 嵌套
alien_0 = {'color': 'red', 'points': 5}
alien_1 = {'color': 'green', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}

aliens = [alien_0,alien_1,alien_2]
print(aliens)
for alien in aliens:
    print(alien)

aliens = []
for number in range(30):
    if number % 2 == 0:
        speed = 'slow'
    else:
        speed = 'medium'
    new_alien = {'color': 'green', 'points': 5, 'speed': speed}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print(len(aliens))