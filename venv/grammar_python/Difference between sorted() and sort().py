# sorted () : This method doesn’t effect the original sequence.

# Python program to demonstrate
# sorted()


L = [5, 6, 8, 5, 9, 3, 6, 2, 9]


print("Sorted list:")
print(sorted(L))

print("\nReverse sorted list:")
print(sorted(L, reverse=True))

# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))

# String-sorted based on ASCII translations
x = 'python'
print(sorted(x))

