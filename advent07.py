# DAY 07
import itertools

def pad(input_value, desired_length):
    return '0'*(desired_length - len(input_value)) + input_value

def pad_and_reverse(input_value, desired_length):
    return pad(input_value, desired_length)[::-1]

def mode_switch(mode, param, intcode):
    if mode == '0':
        return intcode[param]
    else:
        return param

def computer(intcode, input_buffer, output_buffer, comp_position):
    position = comp_position
    
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
            # user_input = input("INPUT VALUE")
            if len(input_buffer) > 0:
                p0 = intcode[position + 1]
                intcode[p0] = int(input_buffer.pop(0))
                position += 2
            else:
                return position
        elif opcode == '04': # user output
            p0 = mode_switch(m0, intcode[position + 1], intcode)
            output_buffer.append(p0)
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
            return position
        else:
            print("UNDEFINED OPCODE", opcode, intcode[position])
            return "UNDEFINED OPCODE"

with open("advent07.txt") as input_file:
    input_string = input_file.readline().split(",")
    intcode = [int(x) for x in input_string]



    
outputs = []
amp_perms = itertools.permutations([5, 6, 7, 8, 9])
for perm in amp_perms:
    amp_a_position = 0
    amp_b_position = 0
    amp_c_position = 0
    amp_d_position = 0
    amp_e_position = 0
    amp_a_input = [perm[0]]
    amp_b_input = [perm[1]]
    amp_c_input = [perm[2]]
    amp_d_input = [perm[3]]
    amp_e_input = [perm[4]]
    amp_a_output = []
    amp_b_output = []
    amp_c_output = []
    amp_d_output = []
    amp_e_output = [0]
    amp_a_intcode = intcode.copy()
    amp_b_intcode = intcode.copy()
    amp_c_intcode = intcode.copy()
    amp_d_intcode = intcode.copy()
    amp_e_intcode = intcode.copy()
    while amp_e_intcode[amp_e_position] != 99:
        amp_a_input.append(amp_e_output.pop(0))
        amp_a_position = computer(amp_a_intcode, amp_a_input, amp_a_output, amp_a_position)
        amp_b_input.append(amp_a_output.pop(0))
        amp_b_position = computer(amp_b_intcode, amp_b_input, amp_b_output, amp_b_position)
        amp_c_input.append(amp_b_output.pop(0))
        amp_c_position = computer(amp_c_intcode, amp_c_input, amp_c_output, amp_c_position)
        amp_d_input.append(amp_c_output.pop(0))
        amp_d_position = computer(amp_d_intcode, amp_d_input, amp_d_output, amp_d_position)
        amp_e_input.append(amp_d_output.pop(0))
        amp_e_position = computer(amp_e_intcode, amp_e_input, amp_e_output, amp_e_position)
    outputs.append(amp_e_output[0])

    
outputs.sort()
print(outputs[-1])=23.-+
0
