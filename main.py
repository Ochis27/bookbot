from stats import number_of_words

def get_book_text(file_path) -> str: 
  """Function to read the text of a book from a file."""
  with open(file_path, 'r', encoding='utf-8') as file:
    file_path = file.read()
  return file_path



def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  number_of_words(book_text)

main()
