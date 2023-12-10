import re
str_list = ['Words', "Sentences"]
sum_str = ''.join(str_list)
result = [re.findall(r'[aeuioAEUIO]', sum_str)]
print(result)