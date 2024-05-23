# Creat an empty set
set = set()


# Add elements to set

set.add(1)
set.add(2)
set.add(3)
set.add(4)
set.add(5)
set.add(6)

print(set)

# Remove elemenst from set
set.remove(1)
set.remove(5)
print(set)

# Remove multiple elemets using a loop
remove_elements = {2, 6}
for element in remove_elements:
    set.remove(element)
    print(set)

    print(f"This set has {len(set)} elemenst.")