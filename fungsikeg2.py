random_list = [31, 4.2, "hei", 10, "ulopyton", 7.2, "universe", 55, 6.7, "AI"]

int_dict = {
    'satuan': [],
    'puluhan': [],
    'ratusan': []
}

float_tuple = ()
string_list = []

for item in random_list:
    if isinstance(item, int):
        if item < 10:
            int_dict['satuan'].append(item)
        elif item < 100:
            int_dict['puluhan'].append(item)
        else:
            int_dict['ratusan'].append(item)
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        string_list.append(item)

print("Data int dlm btk dictionary:")
print(int_dict)
print("\nData float dlm btk tuple:")
print(float_tuple)
print("\nData str dlm btk list:")
print(string_list)
