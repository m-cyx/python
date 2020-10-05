import io #библиотека для кодировки файла
import nltk
from nltk import word_tokenize

f = io.open('input.txt', encoding='utf-8')
text = f.read()
words = word_tokenize(text)
print(words)