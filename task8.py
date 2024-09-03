def merge_dicts(d1, d2):
    merged_dictionary = d1.copy()

    for key, value in d2.items():
        if key in merged_dictionary:
            merged_dictionary[key] += value
        else:
            merged_dictionary[key] = value

    return merged_dictionary

