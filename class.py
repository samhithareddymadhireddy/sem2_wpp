str1="PYthon"
print(str1.swapcase())
str1="python,python,python"

#placeholder works at runtime

#slicing
text="python programming"
reverse=text[::-1]
print(reverse)

import string
print(string.digits)

#regular expression
import re
text="learning python,c++"
pattern=r"[\w+ ,]+"
matches=re.findall(pattern,text)
print(matches)
# result=re.search(pattern,text)
# if result:
#     print("match found at index" ,{result.start()})
# else:
#     print("hi")

