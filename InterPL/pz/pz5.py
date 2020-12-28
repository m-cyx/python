import io
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import download
from nltk.corpus import stopwords

# Открытие файла на чтение
f = io.open('input1.txt', encoding='utf-8')
text = f.read()

# Получаю список список слов
words = word_tokenize(text)

# Открываю на запись слов
f = io.open('result.txt', 'w', encoding='utf-8')
f.write(str(set(words)) + '\n')
print(len(set(words)))
print(len(words))

f.close