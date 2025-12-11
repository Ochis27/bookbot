def number_of_words(text: str) -> str:
  """function to count the number of words in a given text."""
  alpahabet = 'abcdefghijklmnopqrstuvwxyz'
  letters = {}
  text = text.lower()
  for word in text.split():
    for char in word:
      if char in alpahabet:
        letters[char] = letters.get(char, 0) + 1
  print(letters)

