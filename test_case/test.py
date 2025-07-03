
my_dict= {"a":"1", "b":"2"}
for key, value in my_dict.items():
    d = key + '=' + value
    print(d)
    c = '&'.join(d)
print(c)