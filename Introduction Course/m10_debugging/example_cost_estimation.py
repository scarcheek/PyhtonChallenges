# The painter now charges 4.99 € per m**2 wall.
# For the ceiling he charges 5.49 € is the room height is greater than 2.4 meters and 4.99 € otherwise

l = 43.0
w = 23.5
h = 3.2

door_size = 4.0
n_doors = 1
window_size = 3.5
n_windows = 2

wall_area = (l + w) * h * 2
ceiling_area = l * w

wall_area = wall_area - door_size * n_doors - window_size * n_windows

if h > 2.4:
    cost = wall_area * 4.99 + ceiling_area * 5.49
else:
    csot = (wall_area + ceiling_area) * 4.99

print('=' * 40)
print("Estimated Cost: ", round(cost, 2), "€", sep='')
