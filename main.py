import math
import json
import matplotlib.pyplot as plt


with open("data.json") as data_file:
    data = json.load(data_file)

a1 = float(data["a1"])
a2 = float(data["a2"])
distance = float(data["distance"])
delta_t = float(data["delta_t"])

t1 = math.sqrt(2 * distance / (a1 * (1 - a1 / a2)))
t2 = -t1 * a1 / a2
time = t1 + t2
speed_after_acceleration = t1 * a1

current_time = 0.0
current_speed = 0.0
current_position = 0.0

times = []
positions = []
speeds = []

while current_time < t1:
    current_position += current_speed * delta_t

    times.append(current_time)
    positions.append(current_position)
    speeds.append(current_speed)

    current_speed += a1 * delta_t
    current_time += delta_t

while current_time < time:
    current_position += current_speed * delta_t

    times.append(current_time)
    positions.append(current_position)
    speeds.append(current_speed)

    current_speed += a2 * delta_t
    current_time += delta_t

plt.plot(positions, speeds)
plt.xlabel('x(t)')
plt.ylabel('dx/dt')
plt.show()
