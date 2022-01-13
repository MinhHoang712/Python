def count_char(string):
    dict_string = {}
    for item in string:
       dict_string[item] = dict_string.get(item,0)+1
    for f in dict_string.items():
        print(f)
count_char('danghoangminhdhxd')
st = 'danghoangminhdhxd'
print(len(st))
        