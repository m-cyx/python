import io
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import download
from nltk.corpus import stopwords

# Открытие файла на чтение
f = io.open('text.txt', encoding='utf-8')
text = f.read()

# Получаю список предложений и список слов, стоп слов
sentences = nltk.sent_tokenize(text)
words = word_tokenize(text)
stop_words = set(stopwords.words("russian"))

# Запись в файл построчно предложения
f = io.open('result.txt', 'w', encoding='utf-8')
for i in sentences:
    f.write(str(i) + '\n')
# Открываю на дозапись слов и их множества без стоп слов 
f = io.open('result.txt', 'a', encoding='utf-8')
f.write(str(words) + '\n')
nostop = []
# Иду по словам, если слово не в стоп листе, то добавляю к списку слов
for i in words:
    if i not in stop_words:
        nostop.append(i)
# Записываю в файл множество слов из  списка 
f.write(str(set(nostop)))

f.close
