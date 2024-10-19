# basic_arithmetic.py
# Student: Sahar Iqbal
# Date: 10/19/2024
# This program performs basic arithmetic operations (sum, difference, product, and quotient)
# on two numbers provided by the user.

def main():
    """Main function to perform arithmetic operations."""
    # Prompt user for input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Calculate results
        summation = num1 + num2
        difference = num1 - num2
        product = num1 * num2
        
        # Handle division with zero
        if num2 != 0:
            quotient = num1 / num2
        else:
            quotient = "undefined (cannot divide by zero)"
        
        # Print results
        print(f"\nResults:")
        print(f"Sum: {summation}")
        print(f"Difference: {difference}")
        print(f"Product: {product}")
        print(f"Quotient: {quotient}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

