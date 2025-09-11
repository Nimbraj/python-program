
# /d number    /D not number
# /s space    /S not BSPACE
# /w all charters /W not all chatracters

import re

# x="asdsdfgnmfd"
# y=re.findall('[asb]',x)
# print(y)
#
# r="python class"
# u=re.findall("^python",r)
# print(u)
# u1=re.findall("class$",r)
# print(u1)
e="qwertyuioplkjhgfdsazxcvbnmasd7654234567sdds6543sdfg"
r=re.findall(r"[0-9]{4}",e)
print(r)