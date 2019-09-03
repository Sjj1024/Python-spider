fruits = ['app le', 'orange', 'peach']
str = "I want some apples"
if all(str not in element.upper().replace(" ", "") and element.upper().replace(" ", "") not in str for element in fruits):
  print("string contains some fruits")