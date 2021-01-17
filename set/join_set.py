# EX 1
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = set1.union(set2)
print(set3)  # Output: {'c', 'd', 'a', 'e', 'b', 'f'}

# EX 2
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1)  # Output: {'b', 'e', 'c', 'd', 'a', 'f'}
