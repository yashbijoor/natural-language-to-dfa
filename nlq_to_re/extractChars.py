from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
from word2number import w2n

ps = PorterStemmer()

def convert_words_to_numbers(input_str):
  words = input_str.split()
  converted_words = []

  for word in words:
    try:
      # Try to convert the word to a number
      number = w2n.word_to_num(word)
      converted_words.append(str(number))
    except ValueError:
      # If the word is not a number, keep it unchanged
      converted_words.append(word)

  # Join the converted words back into a string
  result_str = ' '.join(converted_words)

  return result_str


def extract_chars(nlp_query):
  wordList = convert_words_to_numbers(nlp_query).split()
  stemmedList = []
  for w in wordList:
    stemmedList.append(ps.stem(w))

  list_of_start_words = ['start', 'begin',]
  list_of_contain_words = ['contain', 'include', 'have']
  list_of_end_words = ['end', 'terminate']

  split_dict = {}

  startList, containList, endList = [], [], []
  flag = 0
  for ch in stemmedList:
    if (ch in list_of_end_words) or flag == 3:
      endList.append(ch)
      flag = 3
    if (ch in list_of_contain_words) or flag == 2:
      containList.append(ch)
      flag = 2
    if (ch in list_of_start_words) or flag == 1:
      startList.append(ch)
      flag = 1
    

  if len(startList) > 1:
    split_dict['start'] = " ".join(startList)
  if len(containList) > 1:
    split_dict['contain'] = " ".join(containList)
  if len(endList) > 1:
    split_dict['end'] = " ".join(endList)

  char_dictionary = {}
  a={}
  b={}
  for i, j in split_dict.items():
    a[i] = re.findall(r"'(.*?)'",j)
    b[i] = re.findall(r"\d+(?:\.\d+)?", j)
    if len(a[i]) != len(b[i]):
      b[i][len(b[i]):] = ['1']*abs(len(a[i])-len(b[i]))

    try:
      char_dictionary[i] = [f"{x}_{y}" for x, y in zip(b[i], a[i])]
    except:
      print("There was an error in extractChars.py")
    
  return char_dictionary