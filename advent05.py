# DAY 05

def pad(input_value, desired_length):
    return '0'*(desired_length - len(input_value)) + input_value

def pad_and_reverse(input_value, desired_length):
    return pad(input_value, desired_length)[::-1]

def mode_switch(mode, param, intcode):
    if mode == '0':
        return intcode[param]
    else:
        return param

def computer(intcode, noun=None, verb=None):
    position = 0
    if noun is not None:
        intcode[1] = noun
    if verb is not None:
        intcode[2] = verb
    while True:
        opcode = pad(str(intcode[position])[-2:], 2)
        mode_segment = pad_and_reverse(str(intcode[position])[:-2], 3)
        m0 = mode_segment[0]
        m1 = mode_segment[1]
        m2 = mode_segment[2]
        if opcode == '01': # addition
            p0 = mode_switch(m0, intcode[position + 1], intcode)
            p1 = mode_switch(m1, intcode[position + 2], intcode)
            p2 = intcode[position + 3]
            intcode[p2] = p0 + p1
            position += 4
        elif opcode == '02': # multiplication
            p0 = mode_switch(m0, intcode[position + 1], intcode)
            p1 = mode_switch(m1, intcode[position + 2], intcode)
            p2 = intcode[position + 3]
            intcode[p2] = p0 * p1
            position += 4
        elif opcode == '03': # user input
            user_input = input("INPUT VALUE")
            p0 = intcode[position + 1]
            intcode[p0] = int(user_input)
            position += 2
        elif opcode == '04': # user output
            p0 = mode_switch(m0, intcode[position + 1], intcode)
            print(p0)
            position += 2
        elif opcode == '05': # jump if not equal to zero 
            p0 = mode_switch(m0, intcode[position + 1], intcode)
            p1 = mode_switch(m1, intcode[position + 2], intcode)
            if p0 != 0:
                position = p1
            else:
                position += 3
        elif opcode == '06': # jump if  equal to zero 
            p0 = mode_switch(m0, intcode[position + 1], intcode)
            p1 = mode_switch(m1, intcode[position + 2], intcode)
            if p0 == 0:
                position = p1
            else:
                position += 3
        elif opcode == '07': # less than
            p0 = mode_switch(m0, intcode[position + 1], intcode)
            p1 = mode_switch(m1, intcode[position + 2], intcode)
            p2 = intcode[position + 3]
            if p0 < p1:
                intcode[p2] = 1
            else:
                intcode[p2] = 0
            position += 4
        elif opcode == '08': # equal to
            p0 = mode_switch(m0, intcode[position + 1], intcode)
            p1 = mode_switch(m1, intcode[position + 2], intcode)
            p2 = intcode[position + 3]
            if p0 == p1:
                intcode[p2] = 1
            else:
                intcode[p2] = 0
            position += 4
        elif opcode == '99':
            return intcode
        else:
            print(opcode, intcode[position])
            return "UNDEFINED OPCODE"

with open("advent05.txt") as input_file:
    input_string = input_file.readline().split(",")
    intcode = [int(x) for x in input_string]
    
newcode = computer(intcode)
print(newcode)