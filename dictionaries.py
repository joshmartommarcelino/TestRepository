import datetime

# Create a dictionary to store book information
book = {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year_published": 1954,
    "genre": "Fantasy"
}

# Access and print the value of the author
print("Author:", book["author"])

# Update the year published to the current year
current_year = datetime.datetime.now().year
book["year_published"] = current_year

print("Updated year of publication:", book["year_published"])

def word_frequency_counter(text):
  """Counts the frequency of words in a given text.

  Args:
    text: The input text.

  Returns:
    A dictionary containing word frequencies.
  """

  words = text.split()
  word_counts = {}

  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

  return word_counts 

if __name__ == "__main__":
  text = input("Enter a text: ")
  word_counts = word_frequency_counter(text)
  print(word_counts)