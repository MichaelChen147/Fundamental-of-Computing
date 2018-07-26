"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    line1 = new_list_zero_end(line) 
    for dummy_i in range(len(line1) - 1):
        if line1[dummy_i] == line1[dummy_i + 1]:
            line1[dummy_i] *= 2
            line1[dummy_i + 1] = 0
    result_list = new_list_zero_end(line1)
    return result_list

def new_list_zero_end(input_list):
    """
    Funtion that end list with zero
    """    
    output_list = list(input_list)
    output_list_index = 0
    for dummy_i in range(len(input_list)):
        output_list[dummy_i] = 0 
    for dummy_i in range(len(input_list)):
        if input_list[dummy_i] > 0:
            output_list[output_list_index] = input_list[dummy_i]
            output_list_index += 1
    
    return output_list


    
#print merge([2, 0, 0, 2])
#print merge([2, 0, 2, 4])
#print merge([0, 0, 2, 2])
#print merge([2, 2, 0, 0] )
#print merge([2, 2, 2, 2, 2])
#print merge([8, 16, 16, 8])
