#!/usr/bin/env python3

# Simplest demonstration of associativity failure
a = 1e16   # Very large number
b = 1.0    # Small number
c = -1e16  # Negative of large number

# Method 1: (a + b) + c
step1 = a + b      # 1e16 + 1 = 1e16 (the 1 is lost due to precision)
left = step1 + c   # 1e16 - 1e16 = 0

# Method 2: a + (b + c)
step2 = b + c      # 1 - 1e16 = -1e16 (approximately)
right = a + step2  # 1e16 - 1e16 = 0

print("Associativity Failure in Floating Point:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print()
print(f"Method 1: (a + b) + c")
print(f"  Step 1: a + b = {a} + {b} = {step1}")
print(f"  Step 2: {step1} + {c} = {left}")
print()
print(f"Method 2: a + (b + c)")
print(f"  Step 1: b + c = {b} + {c} = {step2}")
print(f"  Step 2: {a} + {step2} = {right}")
print()
print(f"Result: (a+b)+c = {left}, a+(b+c) = {right}")
print(f"Equal? {left == right}")
print(f"Expected (mathematically): {b}")