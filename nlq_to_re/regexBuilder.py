import re

class RegexBuilder:
  def __init__(self):
    self.regex = ""
    self.tempList = []

  # For concatenation
  def concat(self, letterList):
    self.tempList.append("(" + "".join(letterList) + ")")
    return self

  def compileRegex(self):
    self.regex += self.tempList[-1]
    self.tempList.clear()
    return self

  # To print the regex
  def printRegex(self):
    print(self.regex)

  # To clear the tempList variable
  def clearTempList(self):
    self.tempList.clear()

  # To append an exact string
  def exactString(self, letter):
    self.tempList.append("(" + letter + ")")
    return self

  # To choose of the characters from a list of possible characters
  def oneOfTheCharacters(self, letterList):
    self.tempList.append("(" + "|".join(letterList) + ")")
    return self

  # To choose any number of characters in any order from a list
  def anyNumberOf(self, letterList):
    self.tempList.append("(" + "*".join(letterList) + "*)*")
    return self

  # To choose any number of characters in a specific order from a list
  def anyNumberOfOrdered(self, letterList):
    self.tempList.append("(" + "*".join(letterList) + "*)")
    return self

  # To append a specific number of characters
  def specificNumberOf(self, letterNumberList):
    self.tempList.append("(" + int(letterNumberList[0])*letterNumberList[1] + ")")
    return self
