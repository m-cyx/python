import io
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import download
from nltk.corpus import stopwords

# Открытие файла на чтение
f = io.open('text1.txt', encoding='utf-8')
text = f.read()

# Получаю список предложений и список слов, стоп слов
sentences = nltk.sent_tokenize(text)
words = word_tokenize(text)
stop_words = set(stopwords.words("russian"))

# Вывожу список стоп слов
print('Список стоп слов: ' + '\n')
print(stopwords.words('russian')) 

# Запись в файл построчно предложения
f = io.open('result.txt', 'w', encoding='utf-8')
f.write('Токенизация по предложениям:' + '\n\n')
for i in sentences:
    f.write(str(i) + '\n')
# Открываю на дозапись слов и их множества без стоп слов 
f = io.open('result.txt', 'a', encoding='utf-8')

f.write( '\n' + 'Токенизация слов:' + '\n')
f.write(str(words) + '\n')
nostop = []
# Иду по словам, если слово не в стоп листе, то добавляю к списку слов
for i in words:
    if i not in stop_words:
        nostop.append(i)
# Записываю в файл множество слов из  списка 

f.write('\n' + 'Множество слов без стоп слов:' + '\n')
f.write(str(set(nostop)))
# Закрываю файл
f.close
