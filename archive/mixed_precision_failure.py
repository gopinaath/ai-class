#!/usr/bin/env python3
"""
Clear demonstration of associativity failure with mixed precision floating point numbers.
"""

import numpy as np

def show_associativity_failure():
    """
    Demonstrates associativity failure using different precision floats.
    """
    print("=" * 70)
    print("ASSOCIATIVITY FAILURE WITH MIXED PRECISION FLOATS")
    print("=" * 70)
    print()

    # Example 1: float32 precision limitations
    print("Example 1: Using float32 (single precision)")
    print("-" * 50)

    # These values chosen to demonstrate precision loss in float32
    a = np.float32(1e7)     # 10,000,000
    b = np.float32(1.0)     # 1
    c = np.float32(-1e7)    # -10,000,000

    # Calculate both ways
    left = np.float32((a + b) + c)
    right = np.float32(a + (b + c))

    print(f"All values are float32 (32-bit, ~7 significant digits)")
    print(f"a = {a:,}")
    print(f"b = {b}")
    print(f"c = {c:,}")
    print()

    print(f"(a + b) + c = ({a} + {b}) + {c}")
    print(f"            = {a + b} + {c}")
    print(f"            = {left}")
    print()

    print(f"a + (b + c) = {a} + ({b} + {c})")
    print(f"            = {a} + {b + c}")
    print(f"            = {right}")
    print()

    print(f"Results: left={left}, right={right}")
    print(f"Are they equal? {left == right}")
    print(f"Difference: {abs(left - right)}")
    print()

    # Example 2: Mixed precision causing issues
    print("Example 2: Mixing float32 and float64")
    print("-" * 50)

    # Mix different precisions
    a_32 = np.float32(16777216)  # 2^24 - exactly representable in float32
    b_64 = np.float64(1.0)        # float64
    c_32 = np.float32(-16777216)  # float32

    # These operations will promote to float64
    left_mixed = (a_32 + b_64) + c_32
    right_mixed = a_32 + (b_64 + c_32)

    print(f"a (float32) = {a_32:,} (2^24)")
    print(f"b (float64) = {b_64}")
    print(f"c (float32) = {c_32:,}")
    print()

    print(f"(a + b) + c = {left_mixed}")
    print(f"a + (b + c) = {right_mixed}")
    print(f"Difference: {abs(left_mixed - right_mixed)}")
    print(f"Are they equal? {left_mixed == right_mixed}")
    print()

    # Example 3: Clear failure case
    print("Example 3: Clear associativity failure")
    print("-" * 50)

    # Use values that clearly demonstrate the problem
    x = 1e20   # Very large
    y = 1.0    # Small
    z = -1e20  # Negative of large

    # Calculate in different orders
    order1 = (x + y) + z
    order2 = x + (y + z)

    print(f"x = {x:e}")
    print(f"y = {y}")
    print(f"z = {z:e}")
    print()

    print(f"Order 1: (x + y) + z")
    print(f"  Step 1: x + y = {x} + {y} = {x + y}")
    print(f"  Step 2: result + z = {x + y} + {z} = {order1}")
    print()

    print(f"Order 2: x + (y + z)")
    print(f"  Step 1: y + z = {y} + {z} = {y + z}")
    print(f"  Step 2: x + result = {x} + {y + z} = {order2}")
    print()

    print(f"Final results:")
    print(f"  (x + y) + z = {order1}")
    print(f"  x + (y + z) = {order2}")
    print(f"  Difference: {abs(order1 - order2)}")
    print(f"  Expected (mathematically): {y}")
    print()

    # Demonstrate with actual mixed precision types
    print("Example 4: Explicit precision conversion effects")
    print("-" * 50)

    # Start with float64, convert to float32, then back
    val64 = np.float64(1.1)
    val32 = np.float32(val64)
    back_to_64 = np.float64(val32)

    print(f"Original float64: {val64:.20f}")
    print(f"Converted to float32: {val32}")
    print(f"Back to float64: {back_to_64:.20f}")
    print(f"Precision lost: {val64 != back_to_64}")
    print(f"Difference: {abs(val64 - back_to_64):e}")
    print()

    # Now show how this affects addition
    a = np.float64(1e8)
    b = np.float32(0.1)  # Will lose precision
    c = np.float64(-1e8)

    result1 = (a + np.float64(b)) + c
    result2 = a + (np.float64(b) + c)

    print(f"With precision loss in b:")
    print(f"a (float64) = {a:e}")
    print(f"b (float32→64) = {np.float64(b):.20f}")
    print(f"c (float64) = {c:e}")
    print()
    print(f"(a + b) + c = {result1:.20f}")
    print(f"a + (b + c) = {result2:.20f}")
    print(f"Difference: {abs(result1 - result2):e}")

if __name__ == "__main__":
    show_associativity_failure()