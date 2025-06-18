"""
Palindrome Number Checker
--------------------------
This script checks whether a given number is a palindrome.

A palindrome number reads the same backward as forward, e.g., 121, 1331, 12321.

Author: Yashwanthi Balaganesan
Date: 2025-06-04

"""

def is_palindrome(number: int) -> bool:
    """
    Returns True if the number is a palindrome, False otherwise.
    
    Args:
        number (int): The number to check.
        
    Returns:
        bool: True if palindrome, False otherwise.
    """
    temp = number
    rev_num = 0

    while number > 0:
        remainder = number % 10
        rev_num = (rev_num * 10) + remainder
        number //= 10

    return temp == rev_num


def main():
    print("Welcome to the Palindrome Number Checker!")
    
    try:
        number = int(input("Enter a number to check: "))
        if number < 0:
            print("Please enter a positive integer.")
            return
        
        if is_palindrome(number):
            print(f"{number} is a palindrome number.")
        else:
            print(f"{number} is not a palindrome number.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
