#collections = counter, namedtuple,ordereddict, defaultdict, deque

from collections import Counter
a = "aaaaabbbbbbccc"
my_Counter = Counter(a)
print(my_Counter.items())
print(my_Counter.keys())
print(my_Counter.values())
print(my_Counter.most_common(1)[0][0])
print(list(my_Counter.elements()))


from collections import namedtuple
ponit = namedtuple('point','x,y')
pt = ponit(1,-4)
print(pt.x , pt.y)


from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
print(ordered_dict)