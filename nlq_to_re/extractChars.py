from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re

ps = PorterStemmer()

def extract_chars(nlp_query):
  wordList = nlp_query.split()
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
  for i, j in split_dict.items():
    char_dictionary[i] = re.findall(r"'(.*?)'",j)
    
  return char_dictionary

