# this program use set methods
s1={2,3,5}
s2={4,2,6,5,3,7}
print(s1.union(s2))
# print(s1.update(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s1.issubset(s2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)