# pattern_drawing.py

# Ask the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to handle each row
while row < size:
    # Use a for loop to print asterisks in one row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after printing one full row
    print()
    # Increment the row counter
    row += 1
