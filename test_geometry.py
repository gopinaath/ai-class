import subprocess
import sys

# Test cases for the geometry calculator
test_cases = [
    ("Test 1: Circle area with radius 5", "1\n5\n4\n"),
    ("Test 2: Rectangle area with length 10 and width 20", "2\n10\n20\n4\n"),
    ("Test 3: Triangle area with base 8 and height 6", "3\n8\n6\n4\n"),
    ("Test 4: Invalid menu choice", "5\n4\n"),
    ("Test 5: Negative radius (should show error)", "1\n-5\n4\n"),
    ("Test 6: Negative rectangle dimensions", "2\n-10\n20\n2\n10\n-20\n4\n"),
]

print("Testing Geometry Calculator")
print("=" * 60)

for test_name, test_input in test_cases:
    print(f"\n{test_name}")
    print("-" * 40)

    result = subprocess.run(
        [sys.executable, 'geometry_calculator.py'],
        input=test_input,
        capture_output=True,
        text=True,
        timeout=5
    )

    print(result.stdout)

    if result.stderr:
        print(f"Error output: {result.stderr}")

print("\n" + "=" * 60)
print("All tests completed!")