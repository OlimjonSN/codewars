import re 
x= "asdfasdf@?da!!!!!!!!sf?"
x=re.sub("[!]", '', x)
print(x)