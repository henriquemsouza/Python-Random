import re

data=open('Pasta1.csv')

texto="oi mundo"

resultado=re.findall(texto, data.read())
print(resultado)
