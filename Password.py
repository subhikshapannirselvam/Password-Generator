import random
def shuffle(string):
    templist=list(string)
    random.shuffle(templist)
    return ''.join(templist)
uppercaseletter1=chr(random.randint(65,90))
uppercaseletter2=chr(random.randint(65,90))
lowercaseletter1=chr(random.randint(97,122))
lowercaseletter2=chr(random.randint(97,122))
num1=chr(random.randint(48,57))
num2=chr(random.randint(48,57))
splchar1=chr(random.randint(33,43))
splchar2=chr(random.randint(33,43))
uppercaseletter3=chr(random.randint(65,90))
lowercaseletter3=chr(random.randint(97,122))
password=uppercaseletter1+uppercaseletter3+uppercaseletter2+lowercaseletter3+lowercaseletter1+lowercaseletter2+num1+num2+splchar1+splchar2
password=shuffle(password)
print(password)
