def calculate_position(pos_movements):
    horizontal_pos = 0
    depth = 0

    for m in pos_movements:
        direction, count = m.strip().split(" ")
        if direction == "forward":
            horizontal_pos += int(count)
        elif direction == "down":
            depth += int(count)
        elif direction == "up":
            depth -= int(count)

    print(f"Horizontal Position: {horizontal_pos}")
    print(f"Depth: {depth}")
    
    return horizontal_pos*depth


with open("navigate_input", 'r') as inF:
    position_instructions = inF.readlines()

final_depth_hor = calculate_position(position_instructions)
print(final_depth_hor)