from keywords import keywords

print(keywords)

reg = "(?:"

for w in keywords :
    reg = reg + w + "|"

reg = reg[:len(reg)-1] + ")"

print(reg)
