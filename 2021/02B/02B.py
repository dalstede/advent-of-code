# changed rules:
# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#    It increases your horizontal position by X units.
#    It increases your depth by your aim multiplied by X

thrust = 0
depth = 0
aim = 0

with open('input.txt', 'r') as file:
    for line in file:
        line_values = line.split(" ")
        direction = line_values[0]
        direction_value = int(line_values[1])

        # pre Python V3.10
        if direction == "forward":
            thrust += direction_value
            depth += direction_value * aim
            
        elif direction == "up":
            aim -= direction_value
        else: # must be "down"
            aim += direction_value

print(thrust * depth)