#tuples

gendres=("Action","Comedy","Drama","Fantasy","Horror","Mystery","Romance","Thriller")
print(gendres)
#its unchangeable and its faster than list
k=(1,2,3,4,5,[6,7,8])
print(k)

#sets
languages={"Python","Java","C++","C#","JavaScript"}
print(languages)
#sets are unordered and unindexed and they are mutable but they do not allow duplicate values
s={1,2,3}
i={3,4,5}
print(s.union(i))
print(s.intersection(i))
print(s.difference(i))

g={1,2,3,4,5,6,7,8,9}
g.add(10)
g.remove(5)
g.pop()
g.discard(3)
print(g)
