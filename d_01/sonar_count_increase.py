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
    inc_count = count_inc(sum_readings)

    return(inc_count)

if __name__ == "__main__":
    # read input file
    with open("sonar_input", 'r') as inF:
        lines = inF.readlines()
        sonar_readings = [int(s) for s in lines]

    # Solution to Part A
    print("Solution to Day 1 Part A")
    inc_count = count_inc(sonar_readings)
    print(f"Depth increase number: {inc_count}\n")

    # Solution to Part B
    print("Solution to Day 2 Part B")
    window = 3
    inc_window_count = count_inc_window(window, sonar_readings)
    print(f"Depth increase over window ({window}): {inc_window_count}\n")