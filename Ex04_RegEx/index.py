import re

text = 'ohjokdshiuokfhsahflsahdfiusa34rnjoisfdjfoj4o35roihsoijj54oijoijsdnn45noinie4o3w43dojisoifj4 useremail@gmail.com'

numbers = re.findall('[0-9]+', text)
email = re.findall('\S+@\S+', text)
print(email)
print(numbers)