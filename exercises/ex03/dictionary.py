"""Testing out dictionary functions and ways to manipulate them."""
___author___ = "730547147"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values of dictionary"""
    flip_diction = dict()
    for keys in dictionary:
        value = dictionary[keys]
        if value in flip_diction:
                raise KeyError("Duplicate key!")  
        flip_diction[value] = keys
    return flip_diction
        

def count(string_list: list[str]) -> dict[str, int]:
    """Counting the amount of times an item shows up in a list."""
    count_dict: dict[str, int] = {}
    for items in string_list:
        if items in count_dict:
            count_dict[items] += 1 
        else:
            count_dict[items] = 1
    return count_dict
            

def favorite_color(people_colors: dict[str, str]) -> str:
    """Returning the most popular color from a list of people."""
    color_list = list()
    for keys in people_colors:
        color_list.append(people_colors[keys])
    color_dictionary = count(color_list)
    max_value = 0
    fav_color = ""
    for colors in color_dictionary:
        if color_dictionary[colors] > max_value:
            max_value = color_dictionary[colors]
            fav_color = colors
    return fav_color


def bin_len(list_string: list[str]) -> dict[int, set[str]]: 
    "Creates dict that contains the length of given strings in a list as int: set."
    len_dict: dict[int, set[str]] = {}
    for values in list_string:
        if len(values) in len_dict:
            len_dict[len(values)].add(values)
        else:
            len_dict[len(values)] = {values}
    return len_dict






