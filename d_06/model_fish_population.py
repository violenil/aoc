from distutils.dep_util import newer_pairwise
from hashlib import new
from itertools import cycle
from turtle import update
from typing import final
from jinja2 import pass_context
import numpy as np

# create array of all original lanternfish
# decrease all numbers by 1
# if one number is now -1, reset it to 6 and add an 8 to the end
# iterate for 80 days
# print length of final array

def read_input(filename):
    with open(filename, 'r') as inF:
        data = list(inF.read().rstrip().split(','))
        fish_ages = np.array([int(a) for a in data], dtype=int)
        print("Number of initial fish: ",len(fish_ages))
    return fish_ages

def cycle_days_inefficient(days, fish_ages):
    for day in range(days):
        new_day_ages = np.subtract(fish_ages, 1)
        renewed = np.where(new_day_ages < 0)
        if renewed[0].size > 0:
            np.add.at(new_day_ages, renewed[0], 7)
            new_fish = np.full(len(renewed[0]), 8, dtype=int)
            updated_fish = np.append(new_day_ages, new_fish)
        else:
            updated_fish = np.copy(new_day_ages)
        fish_ages = np.copy(updated_fish)
        del new_day_ages
        del updated_fish
    return fish_ages

def cycle_days_dict(days: int, fish_ages: dict) -> dict:
    for day in range(days):
        new_fish_ages = {}
        for age, count in fish_ages.items():
            if age == 0:
                new_fish_ages[8] = count
                if 6 in new_fish_ages.keys():
                    new_fish_ages[6] += count
                else:
                    new_fish_ages[6] = count
            else:
                if age-1 in new_fish_ages.keys():
                    new_fish_ages[age-1] += count
                else:
                    new_fish_ages[age-1] = count
        fish_ages = new_fish_ages
    
    return fish_ages

def convert_ages_to_dict(ages: list) -> dict:
    ages_dict = {}
    for age in ages:
        if age in ages_dict.keys():
            ages_dict[age] += 1
        else:
            ages_dict[age] = 1
    return ages_dict

def main():
    fish_ages = read_input("lanternfish_input")
    #fish_ages = [3,4,3,1,2]
    ages_dict = convert_ages_to_dict(fish_ages)
    days = 256
    final_population = cycle_days_dict(days, ages_dict)
    print(f"Number of fish after {days} days: {sum(final_population.values())}")

if __name__ == "__main__":
    main()