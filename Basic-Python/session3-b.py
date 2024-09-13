import re

pattern = r"[aeiou]"
text = "hello , World !"
result = re. findall(pattern,text)
print(result)

pattern = r"[a-z]"
text = "Hello, World !"
result = re.findall(pattern,text)
print(result)

pattern = r"[^a-z]"
text = "Hello, World !"
result = re.findall(pattern,text)
print(result)

pattern = r"[^0-9]"
text = "Hello 1, World !"
result = re.findall(pattern,text)
print(result)

pattern = r"[0-9]"
text = "Hello 1, World !"
result = re.findall(pattern,text)
print(result)

pattern = r"ab?c"
text = "ac"
result = re.search(pattern,text)
print("I am IN ? ")
print(result.group())