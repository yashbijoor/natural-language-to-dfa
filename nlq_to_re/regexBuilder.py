import re

class RegexBuilder:
  def __init__(self):
    self.regex = ""

  def concat(self):
    self.regex += "."
    return self

  def printRegex(self):
    print(self.regex)

  def exactString(self, letter):
    self.regex += letter
    return self

  def oneOfTheCharacters(self, letterList):
    self.regex += "(" + "+".join(letterList) + ")"
    return self

  def anyNumberOf(self, letterList):
    self.regex += "(" + "*".join(letterList) + "*)*"
    return self

  def anyNumberOfOrdered(self, letterList):
    self.regex += "(" + "*".join(letterList) + "*)"
    return self

  def specificNumberOf(self, letter, number):
    self.regex += letter*number
    return self