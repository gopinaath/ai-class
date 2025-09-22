#!/usr/bin/env python3
"""
Celsius to Fahrenheit Temperature Converter
Version: 1.0.0
Author: Temperature Conversion Tool
Date: 2025-01-21

This program converts temperatures from Celsius to Fahrenheit.
Formula: F = (C × 9/5) + 32

Valid input range: -60°C to 200°C
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32


def validate_celsius_input(celsius):
    """
    Validate that Celsius temperature is within acceptable range.

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        bool: True if valid, False otherwise
    """
    MIN_CELSIUS = -60
    MAX_CELSIUS = 200

    if celsius < MIN_CELSIUS or celsius > MAX_CELSIUS:
        print(f"Error: Temperature must be between {MIN_CELSIUS}°C and {MAX_CELSIUS}°C")
        return False
    return True


def main():
    """
    Main program loop for temperature conversion.
    """
    print("=== Celsius to Fahrenheit Temperature Converter ===")
    print("Valid range: -60°C to 200°C\n")

    while True:
        try:
            # Get user input
            celsius_input = input("Enter temperature in Celsius (or 'q' to quit): ")

            # Check for quit command
            if celsius_input.lower() == 'q':
                print("Thank you for using the temperature converter!")
                break

            # Convert input to float
            celsius = float(celsius_input)

            # Validate input range
            if not validate_celsius_input(celsius):
                continue

            # Perform conversion
            fahrenheit = celsius_to_fahrenheit(celsius)

            # Display result
            print(f"{celsius}°C = {fahrenheit:.2f}°F\n")

        except ValueError:
            print("Error: Please enter a valid number or 'q' to quit.\n")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


if __name__ == "__main__":
    main()