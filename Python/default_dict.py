from collections import defaultdict

# default empty dict with int, float and string
int_dict = defaultdict(int)
float_dict = defaultdict(float)
string_dict = defaultdict(str)

# Default dict with list
l_dict = defaultdict(list)
l_dict["New Key"].append("Hello World...")
l_dict["key-1"].append("Value-1")
l_dict["key-2"].append("Value-2")
print(l_dict)

# Default dict with tuple
# Tuple dont have append function but we can replace the value
t_dict = defaultdict(tuple)
t_dict["key-1"] = (1, 2, 3, 4, 5)
print(t_dict)

# Default dict with dict
d_dict = defaultdict(dict)
d_dict["key-2"].update({"key": "value"})
print(d_dict['key-1'])