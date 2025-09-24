import sys
from stats import get_num_words, get_num_chars, sort_chars_dict

def get_book_text(path_to_file):
  file_contents = ""
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents

def main():
  input_list = sys.argv
  if len(input_list) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  book_content = get_book_text(input_list[1])
  get_num_words(book_content)
  unsorted_char_dict = get_num_chars(book_content)
  sorted_list = sort_chars_dict(unsorted_char_dict)
  print("--------- Character Count -------")
  for char_dict in sorted_list:
    if not char_dict["char"].isalpha():
      continue
    print(f"{char_dict['char']}: {char_dict['num']}")
  print("============= END ===============")

main()