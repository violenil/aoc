with open("sonar_input", 'r') as inF:
    lines = inF.readlines()
    sonar_readings = [int(s) for s in lines]

assert type(sonar_readings[10]) == int

def count_inc(readings):
    
    inc_count = 0
    prev = None

    for r in readings:
        if prev == None:
            prev = r
            continue
        if r > prev:
            inc_count += 1
        prev = r
    return(inc_count)

def count_inc_window(window, readings):
    
    assert type(window) == int
    sum_readings = []
    for r in range(len(readings)):
        if r+window > len(readings):
            continue
        sum_window = sum(readings[r:r+window])
        sum_readings.append(sum_window)
    
    print(sum_readings)
    print("number of sums: ", len(sum_readings))

    inc_count = count_inc(sum_readings)

    return(inc_count)


inc_count = count_inc_window(3, sonar_readings)
print(inc_count)