# DAY 04


# find if all digits of password are in order and there is a number that appears exactly twice
def check_double(number):
    str_number = [int(x) for x in str(number)]
    
    sorted_str_number = str_number.sorted() 
    
    if sorted_str_number == str_number: # check for ascending 
        order = True
    else:
        order = False
    
    frequencies = [str_number.count(x) for x in str_number] # repeat values don't matter
    if 2 in frequencies:
        double = True
    else:
        double = False
    return double and order


def find_password_count(lower, upper):
    count = 0
    for i in range(lower, upper+1):
        if check_double(i):
            count += 1
    return count

find_password_count(108457, 562041)
        
