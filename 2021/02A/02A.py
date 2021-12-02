thrust = 0
depth = 0

with open('input.txt', 'r') as file:
    for line in file:
        line_values = line.split(" ")
        direction = line_values[0]
        direction_value = int(line_values[1])

        # pre Python V3.10
        if direction == "forward":
            thrust += direction_value
        elif direction == "up":
            depth -= direction_value
        else: # must be "down"
            depth += direction_value

print(thrust * depth)