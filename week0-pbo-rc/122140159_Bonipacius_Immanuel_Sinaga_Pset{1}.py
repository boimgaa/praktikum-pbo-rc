def print_triangle(height):
    for i in range(1, height + 1):
        # Print spaces for formatting
        print(" " * (height - i), end="")
        # Print '*' for each row
        print("*" * (2 * i - 1))

# Set the height of the triangle
height = 5

# Print the triangle with the specified height
print_triangle(height)
