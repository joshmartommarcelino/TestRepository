def count_letters(sentence):
    """Count the number of letters in a sentence (excluding spaces and punctuation)"""
    letter_count = sum(1 for char in sentence if char.isalpha())
    return letter_count

def main():
    # Getting input from user
    sentence = input("Enter a sentence: ")
    
    # Counts the  letters
    total_letters = count_letters(sentence)
    
    # Displays results
    print(f"\nSentence: '{sentence}'")
    print(f"Total number of letters: {total_letters}")
    
    # Shows breakdown of all characters
    total_chars = len(sentence)
    spaces = sentence.count(' ')
    other_chars = total_chars - total_letters - spaces
    
    print(f"\nBreakdown:")
    print(f"  Letters: {total_letters}")
    print(f"  Spaces: {spaces}")
    print(f"  Other characters (punctuation, numbers, etc.): {other_chars}")
    print(f"  Total characters: {total_chars}")

if __name__ == "__main__":
    main()

# Simple program to print a square in the terminal

# Set the size of sthe square
size = 5

# Prints the square
for row in range(size):
    for col in range(size):
        print("*", end=" ")
    print()  # New line after each row

print()  # Extra line for spacing

# You can also make it interactive: (adjust the size of the shape)
user_size = int(input("Enter square size: "))
print(f"\nSquare of size {user_size}:")

for row in range(user_size):
    for col in range(user_size):
        print("*", end=" ")
    print()