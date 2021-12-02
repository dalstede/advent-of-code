increaseCount = 0

cur_measurement_window = [0, 0, 0]
cur_window_sum = 0
tmp_meaurement_window = [0, 0, 0]
prev_measurement_window = [0, 0, 0]
prev_window_sum = 0
input_number = 0

file = open("input.txt","r") 

for line in file:
    input_number = int(line.rstrip('\n'))

    # build three-measurement windows
        
    prev_measurement_window = cur_measurement_window.copy()
    cur_measurement_window.pop(0)
    cur_measurement_window.append(input_number)
    
    cur_window_sum = cur_measurement_window[0] + cur_measurement_window[1] + cur_measurement_window[2]
    prev_window_sum = prev_measurement_window[0] + prev_measurement_window[1] + prev_measurement_window[2]
    
    print("cur: " + str(cur_measurement_window))
    print("cur: " + str(cur_window_sum))
    print("prev: " + str(prev_measurement_window))
    print("prev: " + str(prev_window_sum))
    
    if prev_measurement_window[0] != 0:
        if cur_window_sum > prev_window_sum:
            increaseCount += 1
    
    print("count: " + str(increaseCount))
    
    print()

print(increaseCount)