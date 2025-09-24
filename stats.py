def get_num_words(content_string):
  words = content_string.split()
  print(f"Found {len(words)} total words")

def get_num_chars(content_string):
  char_occurrence_dict = {}
  for char in content_string:
    char = char.lower()
    if char not in char_occurrence_dict:
      char_occurrence_dict[char] = 1
    else:
      char_occurrence_dict[char] += 1
  return char_occurrence_dict

def sort_on(items):
  return items["num"]

def sort_chars_dict(input_dict):
  list_of_dicts = []
  for char in input_dict:
    mini_dict = {"char": char, "num": input_dict[char]}
    list_of_dicts.append(mini_dict)
  list_of_dicts.sort(reverse=True, key=sort_on)
  return list_of_dicts


