from collections import Counter
from collections import defaultdict
from collections import namedtuple

mylist = [1,1,1,1,1,2,2,2,3,4,4,5]

print(Counter(mylist))

mylist2 = ['a', 'a', 10, 10, 10]
print(Counter(mylist2))

print(Counter('asadsdasdasdasdasd'))

sentence = "How many times does a word show up in this sentence with with a wold"

print(Counter(sentence.lower().split()))


letters = 'aaaaabbbbbbbcccccccc'
c = Counter(letters)
print(c)
print(c.most_common(2))
print(sum(c.values()))                 # total of all counts
print(list(c))                         # list unique elements
print(set(c))                          # convert to a set
print(dict(c))                         # convert to a regular dictionary
print(c.items())                       # convert to a list of (elem, cnt) pairs
#Counter(dict(list_of_pairs))          # convert from a list of (elem, cnt) pairs
#print(c.most_common()[:-n-1:-1])      # n least common elements
#c += Counter()                        # remove zero and negative counts
#print(c.clear())                      # reset all counts


# default dictionary
d = {'a':10}
print(d)
print(d['a'])
#print(d['wrong'])

d = defaultdict(lambda : 0)
print(d)
d['correct'] = 100
print(d['correct'])
print(d['wrong key'])

# named tuples
mytuples = (10, 20, 30)

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=10, breed='Husky', name='Sammy')
print(type(sammy))
print(sammy)
print(sammy.age, sammy.breed, sammy.name)
print(sammy[0], sammy[1], sammy[2])