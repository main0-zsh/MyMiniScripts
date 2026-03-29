import re
pattern=r'\w+\@\w+\.\w+'
text='Электронные адреса:adilhan@email.com, krutoiadil@gmail.com, adilhantwink@mail.ru'
result=re.findall(pattern,text)
print(result)

pattern2=r'\d{3} \d{3} \d{4}'
text2='Mои номера телефона:777 228 1488,425 362 1600'
result2=re.findall(pattern2,text2)
print(result2)

pattern3=r'\d{2}\.\d{2}.\d{4}'
text3='дата моего рождения: 04.06.2012'
result3=re.sub(pattern3,'2012.06.04.',text3)
print(result3)