str1 = 'https://youtu.be/ya_wbCjD9q4'
str1_s = str1.split('/')
str1_s = str1_s[3].split('?')
print(str1_s[0])