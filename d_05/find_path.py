from typing import List, Tuple, Dict
import numpy as np

def read_input(file_name):
    with open(file_name, 'r') as inF:
        lines = inF.readlines()
        coords = [x.strip().split(' -> ') for x in lines]
        int_coords = []
        for x in coords:
            start = list(x[0].split(','))
            s = [int(x) for x in start]
            end = list(x[1].split(','))
            e = [int(x) for x in end]
            int_coords.append([list(s),list(e)])
    return int_coords

def is_diag(line):
    if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
        return True
    else: return False

def find_line_points(x1, y1, x2, y2):
    x_points = []
    y_points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2: # in reverse
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            x_points.append(y)
            y_points.append(x)
        else:
            x_points.append(x)
            y_points.append(y)
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    return x_points, y_points

def update_matrix(matrix, line_coords, no_diag: True):
    for line in line_coords:
        if no_diag:
            if is_diag(line):
                continue
        start, end = line
        x1, y1 = start
        x2, y2, = end
        #if is_horizontal(line) or is_vertical(line):
        x_points, y_points = find_line_points(x1, y1, x2, y2)
        np.add.at(matrix, [x_points, y_points], 1)
    return matrix

def main():
    map = np.zeros((1000, 1000), dtype=int)

    line_coords = read_input("thermal_input")

    map = update_matrix(map, line_coords, no_diag=False)

    print(len(map[map>=2]))

if __name__ == "__main__":
    main()