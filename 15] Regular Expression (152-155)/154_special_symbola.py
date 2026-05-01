#uising regular expression find out only special symbol from gven string
import re
s="@prathamesh$"
pattern=r"\W"
print(re.findall(pattern,s))