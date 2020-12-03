import io
import nltk 
from nltk.corpus import stopwords 
from pymorphy2 import MorphAnalyzer  
morph = MorphAnalyzer() # Для удобства использования, в дельнейшем, будем сокращать название этого метода.

# Открытие файла на чтение
f = io.open('dataset.txt', encoding='utf-8')
text = f.read()

# Удаляю стоп слова  
stop_words = set(stopwords.words('russian'))  # Стоп-слова 
words = nltk.word_tokenize(text)
# Возвращаю все слова с понижением регистра если они не в стоп листе и не содержат знаков препинания
nostop = set([word.lower() for word in words if word not in stop_words and word.isalnum()])

# Морфологический анализатор
result = [] 
for word in nostop: 
    p = morph.parse(word)[0] 
    result.append(  "Исходное слово: "                  + word + 
                    "\nНормальная форма: "              + str(p.normal_form) + 
                    "\nМорфологический разбор слова: "  + p.tag.cyr_repr + '\n\n') #перевожу теги на киррилицу 

# Определяю кол-во обработанных слов
counter_0 = str(len(words))  # слова до удаления стоп-слов
counter_1 = str(len(nostop)) # слова для разбора

# Записываю результат в файл
f = io.open('result2.txt', 'w', encoding='utf-8')
f.write('Количество слов до "отчистки": ' + counter_0 + '\n')
f.write('Обработано слов:               ' + counter_1 + '\n\n')

f.write(''.join(result))
f.close

'''
Примечание: 
    Каждый новый вывод будет иметь отличный от предыдущего порядок.
    Это связано с тем, что объекты множества не упорядочены.
'''