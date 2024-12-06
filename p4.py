# Python program to generate Fibonacci series

# Input: Getting the number of terms from the user
n_terms = int(input("Enter the number of terms for the Fibonacci series: "))

# Initializing the first two terms
a, b = 0, 1

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print(f"Fibonacci series: {a}")
else:
    print("Fibonacci series:")
    print(a, b, end=" ")  # Print the first two terms
    
    # Generate the Fibonacci series
    for _ in range(2, n_terms):
        next_term = a + b
        print(next_term, end=" ")
        a, b = b, next_term  # Update the terms
