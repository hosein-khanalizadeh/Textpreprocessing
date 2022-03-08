# -*- coding: utf-8 -*-

"""
Created on Mon March 2022

@author: Hosein Khanalizadeh

"""

# کتابخانه ها
import re
import nltk


# باز کردن متن
input_str = open('data.txt', 'r').read()
print('متن اصلی : \n' , input_str)

print('-----------------------------------')

# تبدیل متن به حروف کوچک
input_str = input_str.lower()
print('تبدیل متن به حروف کوچک : \n' , input_str)

print('-----------------------------------')

# پاک کردن اعداد از داده‌های متنی
input_str = re.sub(r'\d+','',input_str)
print('حذف اعداد : \n' , input_str)

print('-----------------------------------')

# پاک کردن علائم نقطه گذاری
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ''
for char in input_str:
   if char not in punctuations:
       no_punct = no_punct + char
input_str = no_punct
print('حذف علائم : \n' , input_str)

print('-----------------------------------')

# پاک کردن فضاهای خالی
input_str = re.sub(' +', ' ', input_str)
# input_str = input_str.split()
# input_str = ' '.join(input_str)
print('حذف فضای خالی : \n' , input_str)

print('-----------------------------------')

# جداسازی واژگان
tokens = nltk.tokenize.word_tokenize(input_str)
print('لیست کردن واژگان : \n' , input_str)

print('-----------------------------------')

# حذف واژه های اسپارس
stop_words = set(nltk.corpus.stopwords.words('english'))
result = [i for i in tokens if not i in stop_words]
print('حذف واژگان اسپارس : \n' , input_str)

print('-----------------------------------')

# ریشه یابی کلمات 1
stemmer = nltk.stem.PorterStemmer()
print('ریشه یابی ساقه : \n')
for word in tokens:
    print(word , ' : ' , stemmer.stem(word))

print('-----------------------------------')

# ریشه یابی کلمات 2
lemmatizer = nltk.stem.WordNetLemmatizer()
print('ریشه یابی لماتیزه کننده : \n')
for word in tokens:
    print(word , ' : ' , lemmatizer.lemmatize(word))

print('-----------------------------------')

# برچسب گذاری نقش دستوری
print('برپسب گذاری نقش دستوری : \n')
tokenized = nltk.tokenize.sent_tokenize(input_str)
for i in tokenized:
    wordsList = nltk.tokenize.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words]
    tagged = nltk.pos_tag(wordsList)
    print(tagged)

print('-----------------------------------')

# تجزیه و تحلیل سطحی جملات (تقطیع)
reg_exp = 'NP: {<DT>?<JJ>*<NN>}'
rp = nltk.RegexpParser(reg_exp)
result = rp.parse(tagged)
print('تقطیع : \n' , result)
# result.draw()

print('-----------------------------------')

# بازشناسی موجودیت نامدار
result = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(input_str)))
print('بازشناسی موجودیت نامدار : \n' , result)

print('-----------------------------------')
