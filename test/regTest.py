import re

str = "lucid"
# 忽略大小写
result = re.search("luqidd", str, re.IGNORECASE)
print(result)
print(result.string)
print(len(result.string) is None)