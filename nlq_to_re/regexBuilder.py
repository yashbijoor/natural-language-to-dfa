import re

class RegexBuilder:
  def __init__(self):
    self.regex = ""
    self.tempList = []

  # For concatenation
  def concat(self, letterList):
    self.tempList.append("(" + "".join(letterList) + ")")
    return self

  # To compile the regex (The last element of the tempList gets added to regex)
  def compileRegex(self):
    self.regex += self.tempList[-1]
    return self

  # To print the regex
  def printRegex(self):
    print(self.regex)

  # To clear the tempList variable
  def clearTempList(self):
    self.tempList.clear()
    return self

  # To clear the tempList partially (Index defines the number of elements to pop from the end of tempList variable)
  def clearTempListPartially(self, index):
    self.tempList = self.tempList[:len(self.tempList)-index]
    return self

  # To append an exact string. If letter is 'a' then the output will be (a)
  def exactString(self, letter):
    self.tempList.append("(" + letter + ")")
    return self

  # To choose of the characters from a list of possible characters. If letterList is ['a','b','c'] then the output will be (a|b|c)
  def oneOfTheCharacters(self, letterList):
    self.tempList.append("(" + "|".join(letterList) + ")")
    return self

  # To choose any number of characters in any order from a list. If letterList is ['a','b','c'] then the output will be (a*b*c*)*
  def anyNumberOf(self, letterList):
    self.tempList.append("((" + "*".join(letterList) + "*)*)")
    return self

  # To choose any number of characters in a specific order from a list. If letterList is ['a','b','c'] then the output will be (a*b*c*)
  def anyNumberOfOrdered(self, letterList):
    self.tempList.append("(" + "*".join(letterList) + "*)")
    return self

  # To append a specific number of characters. If letterNumberList is [3,'a'] then the output will be (aaa)
  def specificNumberOf(self, letterNumberList):
    self.tempList.append("(" + int(letterNumberList[0])*letterNumberList[1] + ")")
    return self
  
  # To handle atmost case. For example if letterNumberList is [3,'a'] then the output will be (a|aa|aaa)
  def atmost(self, letterNumberList):
    i = 1
    output = "(" + letterNumberList[1] + ")"
    while i < int(letterNumberList[0]):
      i += 1
      output += "|" + "(" + letterNumberList[1] * i + ")"
    self.tempList.append("(" + output + ")")
    return self

  # To handle 'EVEN' case. If letter is 'a' then output will be 2*a i.e. (aa)*
  def even(self, letter):
    self.tempList.append("(" + letter*2 + ")*")
  
  # To handle 'ODD' case. If letter is 'a' then output will be 2*a i.e. (aa)*a
  def odd(self, letter):
    self.tempList.append("(" + letter*2 + ")*" + letter)

  # Just adds * to the letter. If letter is 'a' the returns (a)*
  def loop(self, letter):
    self.tempList.append("(" + letter + ")*")
