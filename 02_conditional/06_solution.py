# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).


distance = 10

if distance < 3:
    mode_of_transportation = "Walk"
elif distance < 15:
    mode_of_transportation = 'Bike'
elif distance > 15:
    mode_of_transportation = "Car"
print(mode_of_transportation)