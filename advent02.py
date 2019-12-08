# DAY 02
def computer(intcode, noun=None, verb=None): # verb and noun are used as possible inputs for part 2
    position = 0
    if noun is not None:
        intcode[1] = noun
    if verb is not None:
        intcode[2] = verb
    while True: # main execution loop
        if intcode[position] == 1: # addition operator
            intcode[intcode[position + 3]] = intcode[intcode[position + 1]] + intcode[intcode[position + 2]]
        elif intcode[position] == 2: # multiplication operator
            intcode[intcode[position + 3]] = intcode[intcode[position + 1]] * intcode[intcode[position + 2]]
        elif intcode[position] == 99: # halt operator
            return intcode
        else:
            return "UNDEFINED OPCODE"
        position += 4

with open("advent02.txt") as input_file:
    input_string = input_file.readline().split(",")
    intcode = [int(x) for x in input_string]
    
# find a specific intcode
for i in range(0, 100):
    for j in range(0, 100):
        return_intcode = computer(intcode.copy(), noun=i, verb=j)
        if return_intcode[0] == 19690720: # hard coded specific goal
            print(i, j)
            break