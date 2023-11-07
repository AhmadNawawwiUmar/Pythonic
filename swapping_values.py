# cara konvensional pertukaran nilai antar variable

# a = 10
# b = 20
# print("sebelum pertukaran")
# print(f"a = {a}, b = {b}")

# c = a
# a = b
# b = c
# print("setelah pertukaran")
# print(f"a = {a}, b = {b}")

# cara yang lebih pythonic pertukaran nilai antar variable

a, b, c, d, e = 10, 20, 30, 40, 50

print("sebelum pertukaran")
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")

a, b, c, d, e = b, e, a, c, a

print("setelah pertukaran")
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
