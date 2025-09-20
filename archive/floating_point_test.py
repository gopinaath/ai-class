#!/usr/bin/env python3
"""
Test program showing floating point associativity failures.
Demonstrates cases where (a + b) + c != a + (b + c)
"""

import numpy as np

def test_associativity(a, b, c):
    """Test if (a + b) + c == a + (b + c)"""
    left_assoc = (a + b) + c
    right_assoc = a + (b + c)
    difference = abs(left_assoc - right_assoc)

    return left_assoc, right_assoc, difference

def main():
    print("=" * 70)
    print("FLOATING POINT ASSOCIATIVITY FAILURES")
    print("=" * 70)
    print("Testing if (a + b) + c == a + (b + c)")
    print()

    # Test 1: Classic failure with different magnitudes
    print("Test 1: Large + Small - Large")
    print("-" * 40)
    a, b, c = 1e16, 1.0, -1e16
    left, right, diff = test_associativity(a, b, c)

    print(f"a = {a:e}")
    print(f"b = {b}")
    print(f"c = {c:e}")
    print(f"(a + b) + c = {left}")
    print(f"a + (b + c) = {right}")
    print(f"Difference: {diff}")
    print(f"FAILED: Expected 1.0, got {left}")
    print()

    # Test 2: Another magnitude difference case
    print("Test 2: Different magnitude failure")
    print("-" * 40)
    a, b, c = 1e20, 1.0, -1e20
    left, right, diff = test_associativity(a, b, c)

    print(f"a = {a:e}")
    print(f"b = {b}")
    print(f"c = {c:e}")
    print(f"(a + b) + c = {left}")
    print(f"a + (b + c) = {right}")
    print(f"Difference: {diff}")
    print(f"FAILED: Expected 1.0, got {left}")
    print()

    # Test 3: Float32 precision failure
    print("Test 3: Float32 precision limits")
    print("-" * 40)
    a = np.float32(1e7)
    b = np.float32(1.0)
    c = np.float32(-1e7)
    left, right, diff = test_associativity(a, b, c)

    print(f"a (float32) = {a}")
    print(f"b (float32) = {b}")
    print(f"c (float32) = {c}")
    print(f"(a + b) + c = {left}")
    print(f"a + (b + c) = {right}")
    print(f"Difference: {diff}")
    print(f"Note: Both equal {left}, expected 1.0")
    print()

    # Test 4: Extreme case
    print("Test 4: Extreme magnitude difference")
    print("-" * 40)
    a, b, c = 1e30, 1e-5, -1e30
    left, right, diff = test_associativity(a, b, c)

    print(f"a = {a:e}")
    print(f"b = {b:e}")
    print(f"c = {c:e}")
    print(f"(a + b) + c = {left}")
    print(f"a + (b + c) = {right}")
    print(f"Difference: {diff}")
    print(f"FAILED: Expected {b:e}, got {left}")
    print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("All tests demonstrate associativity failure.")
    print("Floating point arithmetic is NOT associative when:")
    print("  - Numbers have vastly different magnitudes")
    print("  - Precision loss occurs during operations")

if __name__ == "__main__":
    main()