def calculate_position(pos_movements, aim:int=0, use_aim:bool=False):
    horizontal_pos = 0
    depth = 0

    for m in pos_movements:
        direction, count = m.strip().split(" ")
        if direction == "forward":
            horizontal_pos += int(count)
            if use_aim:
                depth += int(count)*aim

        elif direction == "down":
            if use_aim:
                aim += int(count)
            else:
                depth += int(count)

        elif direction == "up":
            if use_aim:
                aim -= int(count)
            else:
                depth -= int(count)
    print(f"Horizontal Position: {horizontal_pos}")
    print(f"Depth: {depth}")
    return horizontal_pos*depth

with open("navigate_input", 'r') as inF:
    position_instructions = inF.readlines()


if __name__ == "__main__":
    # To solve Part A:
    print("Solution to Day 02 Part A")
    final_depth_hor = calculate_position(position_instructions, use_aim=False)
    print(f"Final solution: {final_depth_hor}\n")

    # To solve Part B:
    print("Solution to Day 02 Part B")
    final_depth_hor = calculate_position(position_instructions, use_aim=True)
    print(f"Final solution: {final_depth_hor}\n")