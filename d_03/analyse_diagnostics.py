from typing import List

def find_gamma_rate(bin_list: List):
    gamma_rate = ""
    for i in range(12):
        bit_list = [x[i] for x in bin_list]
        most_freq = max(set(bit_list), key = bit_list.count)
        gamma_rate = gamma_rate + most_freq

    return gamma_rate

def find_epsilon_rate(bin_list: List):
    epsilon_rate = ""
    for i in range(12):
        bit_list = [x[i] for x in bin_list]
        least_freq = min(set(bit_list), key = bit_list.count)
        epsilon_rate = epsilon_rate + least_freq
    
    return epsilon_rate

def find_ox_gen_rating(bin_list: List):
    for i in range(12):
        bit_list = [x[i] for x in bin_list]
        if bit_list.count('0') == bit_list.count('1'):
            most_freq = '1'
        else:
            most_freq = max(set(bit_list), key = bit_list.count)
        matching_bins = [x for x in bin_list if x[i] == most_freq]
        if len(matching_bins) == 1: # only 1 bin left
            return matching_bins[0]
        else:
            bin_list = matching_bins

def find_co2_scrub_rating(bin_list: List):
    for i in range(12):
        bit_list = [x[i] for x in bin_list]
        if bit_list.count('0') == bit_list.count('1'):
            least_freq = '0'
        else:
            least_freq = min(set(bit_list), key = bit_list.count)
        matching_bins = [x for x in bin_list if x[i] == least_freq]
        if len(matching_bins) == 1: # only one bin left
            return matching_bins[0]
        else:
            bin_list = matching_bins


if __name__=="__main__":
    with open("diagnostic_report", 'r') as inF:
            diagnostic_bin = inF.readlines()

    # Solution to Day 3 Part A
    print("Solution for Part A")
    gamma = find_gamma_rate(diagnostic_bin)
    epsilon = find_epsilon_rate(diagnostic_bin)
    print(f"Gamma Rate: {gamma} ({int(gamma,2)})")
    print(f"Epsilon Rate: {epsilon} ({int(epsilon, 2)})")
    power_consumption = int(gamma, 2)*int(epsilon, 2)
    print(f"Power Consumption: {power_consumption}")
    print()

    # Solution to Day 3 Part B
    print("Solution for Part B")
    ox_gen = find_ox_gen_rating(diagnostic_bin)
    co2_scrub = find_co2_scrub_rating(diagnostic_bin)
    print(f"Oxygen Generator Rate: {ox_gen} ({int(ox_gen,2)})")
    print(f"CO2 Scrubber Rate: {co2_scrub} ({int(co2_scrub,2)})")
    life_support_rating = int(co2_scrub,2)*int(ox_gen,  2)
    print(f"Life Support Rate: {life_support_rating}")
    print()