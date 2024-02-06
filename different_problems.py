# def merge_dicts(dict1, dict2):
#     merged_dict = dict1.copy()

#     for key, value in dict2.items():
#         if key in merged_dict:
#             merged_dict[key] = [merged_dict[key], value] if isinstance(merged_dict[key], (list, tuple)) else [merged_dict[key], value]
#         else:
#             merged_dict[key] = value

#     return merged_dict

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}

# result = merge_dicts(dict1, dict2)
# print(result)



from collections import defaultdict

def merge_dicts(dict1, dict2):
    merged_dict = defaultdict(list)

    for d in (dict1, dict2):
        for key, value in d.items():
            merged_dict[key].append(value)

    return {key: value[0] if len(value) == 1 else value for key, value in merged_dict.items()}

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

result = merge_dicts(dict1, dict2)
print(result)


