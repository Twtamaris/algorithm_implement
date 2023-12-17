def find_erc_pairs(x, y):
    list2 = []
    for a in range(1, x+1):
        for b in range(1, min(a, y+1)):  # b should be less than or equal to a and y
            if a // b == a % b:
                list2.append((a, b))
    return list2

# Test the function
x = 303578353
y = 24778
list2 = find_erc_pairs(x, y)
print(f"ERC pairs between {x} and {y} are: {list2}")
print("This is the length")
print(len(list2))
