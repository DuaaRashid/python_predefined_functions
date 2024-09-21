# 3-10. Every Function
favorite_novels : list =["namal","aks","hasil","la hasil","iblees","mala","halim"]
# print([i for i in dir(list) if "__" not in i])
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(f'\t\tFavorite Novels')
print(favorite_novels)

favorite_novels.append("ishq atish")
print(f"Append method: {favorite_novels}")
copy : list =favorite_novels.copy()

copy.pop()
print(f"Copy method makes a shallow copy {copy}")
print(f"Original list: {favorite_novels}")
print(f"Pop Method(removes the last value and returns it):{favorite_novels.pop()}")
print(f"Original list: {favorite_novels}")

favorite_novels.extend(["jannat k pattay","peer e kamil","ab e hayat"])
print(f"Extend Method:{favorite_novels}")
print(f"Count Method(counts number of elements present in a list): {favorite_novels.count("namal")}")
print(f"Index Method(returns the index number of element): {favorite_novels.index("mala")}")

favorite_novels.insert(10,"ishq atish")
print(f"Insert Method(adds element in the list at the given index): {favorite_novels}")

favorite_novels.remove("mala")
print(f"Remove Method(removes given element): {favorite_novels}")

favorite_novels.reverse()
print(f"Reverse Method: {favorite_novels}")

favorite_novels.sort()
print(f"Sort Method: {favorite_novels}")
