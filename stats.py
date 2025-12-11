def number_of_words(text: str) -> str:
  """function to count the number of words in a given text."""
  num_words = 0
  for word in text.split():
    num_words += 1
  print(f"Found {num_words} total words")