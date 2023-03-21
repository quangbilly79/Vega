lst = [["a ", "b  "], ["c ", "d  "], ["z"], ["e  ", "f"], [" g"], ["h", "e", "f"]]

my_dict = {}
special_sublist_dict = {}

for i, sublst in enumerate(lst):
    if len(sublst) == 2: # Normal case, there are 2 values in a list
        key = sublst[0].strip()
        value = sublst[1].strip()
        my_dict[key] = value
    elif len(sublst) != 2: # Special case, for example 1 or 3 value in a list
        key = sublst[0].strip() # Set the value in the list be the key of the dict
        my_dict[key] = "special_case" # The value of the dict is a character you choose

        # Get the position and value of special case in original list
        special_case_index = i
        special_sublist_dict.update({special_case_index: lst[special_case_index]})

print(my_dict) # {'a': 'b', 'c': 'd', 'z': 'special_case', 'e': 'f', 'g': 'special_case', 'h': 'special_case'}
print(special_sublist_dict) # {2: ['z'], 4: [' g'], 5: ['h', 'e', 'f']}. Position and value of special case

