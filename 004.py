"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def findPalindrome(): # Define function to return value
    upp = 999 * 999; low = 100 * 100    # Identify the lowest and highest 3-digit numbers
    for i in reversed(range(low,upp)):
        n_str = str(i)
        if n_str == n_str[::-1]:        # Identify if palindrome
            for j in range(100,1000):   # Range for 3-digit multiples
                # Check if multiple and if the other multiple is also 3 digits
                if (i%j == 0) and (len(str(int(i/j))) == 3):
                    print(i)
                    return

findPalindrome()