#!/usr/bin/env python3
"""
Demonstration of floating point associativity failure with different precision numbers.

This program shows how (a + b) + c != a + (b + c) when numbers have vastly different magnitudes.
"""

import numpy as np

def demonstrate_associativity_failure():
    """
    Show a clear example where floating point addition is not associative.
    """
    print("=" * 70)
    print("FLOATING POINT ASSOCIATIVITY FAILURE DEMONSTRATION")
    print("=" * 70)
    print()

    # Classic example: Large + Small - Large
    print("Example 1: Classic failure with different magnitudes")
    print("-" * 50)

    # Using regular Python floats (64-bit)
    a = 1e16   # Very large number (larger to ensure precision loss)
    b = 1.0    # Small number (compared to a)
    c = -1e16  # Negative of the large number

    # Calculate both ways
    left_assoc = (a + b) + c   # (1e15 + 1) - 1e15
    right_assoc = a + (b + c)  # 1e15 + (1 - 1e15)

    print(f"a = {a:e} (large positive)")
    print(f"b = {b:e} (small)")
    print(f"c = {c:e} (large negative)")
    print()

    print(f"(a + b) + c = ({a:e} + {b:e}) + {c:e}")
    print(f"            = {a + b:e} + {c:e}")
    print(f"            = {left_assoc}")
    print()

    print(f"a + (b + c) = {a:e} + ({b:e} + {c:e})")
    print(f"            = {a:e} + {b + c:e}")
    print(f"            = {right_assoc}")
    print()

    print(f"Difference: {abs(left_assoc - right_assoc)}")
    print(f"Are they equal? {left_assoc == right_assoc}")
    print()

    # Example 2: Using different precision types
    print("Example 2: Mixed precision types (float32 vs float64)")
    print("-" * 50)

    # Create numbers with different precisions
    a_32 = np.float32(1e7)    # 32-bit float
    b_64 = np.float64(0.001)  # 64-bit float
    c_32 = np.float32(-1e7)   # 32-bit float

    # Calculate both ways (results will be promoted to float64)
    left_mixed = (a_32 + b_64) + c_32
    right_mixed = a_32 + (b_64 + c_32)

    print(f"a (float32) = {a_32} (precision: ~7 decimal digits)")
    print(f"b (float64) = {b_64} (precision: ~15 decimal digits)")
    print(f"c (float32) = {c_32}")
    print()

    print(f"(a + b) + c = {left_mixed}")
    print(f"a + (b + c) = {right_mixed}")
    print(f"Difference: {abs(left_mixed - right_mixed)}")
    print(f"Are they equal? {left_mixed == right_mixed}")
    print()

    # Example 3: Demonstrating precision loss
    print("Example 3: Step-by-step precision loss")
    print("-" * 50)

    # Show how precision is lost in each step
    large = 1e16
    small = 1.0

    print(f"Starting values:")
    print(f"  large = {large:e}")
    print(f"  small = {small:e}")
    print()

    # Method 1: Add small to large first
    print("Method 1: (large + small) - large")
    step1_m1 = large + small
    print(f"  Step 1: large + small = {step1_m1:e}")
    print(f"          Exact value should be {large + 1:e}")
    print(f"          But due to precision: {step1_m1:e}")
    step2_m1 = step1_m1 - large
    print(f"  Step 2: result - large = {step2_m1}")
    print()

    # Method 2: Compute the difference first
    print("Method 2: large + (small - large)")
    step1_m2 = small - large
    print(f"  Step 1: small - large = {step1_m2:e}")
    step2_m2 = large + step1_m2
    print(f"  Step 2: large + result = {step2_m2}")
    print()

    print(f"Final results:")
    print(f"  Method 1 result: {step2_m1}")
    print(f"  Method 2 result: {step2_m2}")
    print(f"  Expected result: {small}")
    print()

    # Explanation
    print("=" * 70)
    print("EXPLANATION")
    print("=" * 70)
    print("""
The associativity failure occurs because:

1. Floating point numbers have limited precision (mantissa bits)
2. When adding a very large and very small number, the small number's
   contribution may be lost due to rounding
3. The order of operations matters when precision loss occurs

In Example 1:
- (1e15 + 1) rounds to 1e15 (the 1 is lost)
- Then 1e15 - 1e15 = 0
- But 1 + (-1e15) = -999999999999999 (approximately)
- Then 1e15 + (-999999999999999) = 1

This demonstrates that floating point arithmetic is NOT associative,
particularly when dealing with numbers of vastly different magnitudes.
""")

if __name__ == "__main__":
    demonstrate_associativity_failure()