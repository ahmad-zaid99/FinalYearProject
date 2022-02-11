import re
from keywords import keywords

# print(keywords)

reg = "(?:"

for w in keywords :
    reg = reg + w + "|"

reg = reg[:len(reg)-1] + ")"

# lst = re.findall("[\d\.]*\d+", "I have 29 cats and 39 dogs.")
print(len(re.findall("[\d\.]*\d+", "I have 29 cats and 39 dogs.")))

# print(reg)
