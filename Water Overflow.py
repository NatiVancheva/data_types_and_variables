number_of_lines = int(input())
tank_capacity = 255
for current_line in range(number_of_lines):
    litters_of_water = int(input())
    if tank_capacity < litters_of_water:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litters_of_water
print(255 - tank_capacity)