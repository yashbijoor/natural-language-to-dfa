import re

class RegexBuilder:
  def __init__(self):
    self.regex = ""

  # For concatenation
  def concat(self):
    self.regex += "."
    return self

  # To print the regex
  def printRegex(self):
    print(self.regex)

  # To append an exact string 
  def exactString(self, letter):
    self.regex += letter
    return self

  # To choose of the characters from a list of possible characters
  def oneOfTheCharacters(self, letterList):
    self.regex += "(" + "|".join(letterList) + ")"
    return self

  # To choose any number of characters in any order from a list
  def anyNumberOf(self, letterList):
    self.regex += "(" + "*".join(letterList) + "*)*"
    return self

  # To choose any number of characters in a specific order from a list
  def anyNumberOfOrdered(self, letterList):
    self.regex += "(" + "*".join(letterList) + "*)"
    return self

  # To append a specific number of characters
  def specificNumberOf(self, letterNumberList):
    self.regex += int(letterNumberList[0])*letterNumberList[1]
    return self