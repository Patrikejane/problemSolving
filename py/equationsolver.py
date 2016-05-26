import re
s = input('What is your math problem? ')
if re.findall('\d+? *?\+ *?\d+?', s):
  print (eval(s))
else:
  print ("Try entering a math problem")
