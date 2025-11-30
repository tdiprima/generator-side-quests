# Demonstrates that generators are one-time use and cannot be reused
# without recreation.


def numbers():
    for i in range(5):
        yield i


gen = numbers()

# First iteration
for n in gen:
    print(n)  # prints 0 to 4

# Second iteration (nothing happens)
for n in gen:
    print(n)  # nothing prints

# Recreate to use again
gen = numbers()
for n in gen:
    print(n)  # prints 0 to 4 again
