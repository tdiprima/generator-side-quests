# Demonstrates how generators appear when printed and must be iterated
# to view contents.

gen = (x * x for x in range(5))
print(gen)  # Shows generator object

# To view contents
for value in gen:
    print(value)
