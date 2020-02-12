import collections
import json

tree = lambda: collections.defaultdict(tree)
dict = tree()
dict['color']['fav'] = 'red'
print(json.dumps(dict))
