from collections import defaultdict

my_dict=defaultdict(lambda:'nothing')
my_dict['one']='green'
print(my_dict['two'])
print(my_dict)