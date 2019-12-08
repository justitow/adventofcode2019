# DAY 01
import math



def fuel_for_fuel(input_fuel):
    extra = math.floor(int(input_fuel)/3)-2
    if extra <= 0:
        return 0
    else:
        return extra + fuel_for_fuel(extra) # recursively add on the chunk of fuel


total_fuel = 0
with open("advent01.txt") as input_file:
    for row in input_file:
        total_fuel += math.floor(int(row)/3)-2 + fuel_for_fuel(math.floor(int(row)/3)-2)
print(total_fuel)


        