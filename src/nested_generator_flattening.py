# Demonstrates flattening nested lists using yield from for cleaner generator code.

list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]


def flat_gen():
    for sublist in list_of_lists:
        yield from sublist


# Usage
for item in flat_gen():
    print(item)
