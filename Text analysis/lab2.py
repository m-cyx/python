import io
import nltk 
from nltk.corpus import stopwords 
from pymorphy2 import MorphAnalyzer 

# Морфологический анализатор 
morph = MorphAnalyzer() 


# Считывание текста 
with open('text1.txt', 'r') as read_file: 
    text = read_file.readlines() 
text = '\n'.join(text) 

# Открытие файла на чтение
f = io.open('text1.txt', encoding='utf-8')
text = f.read()



# Удаление из текста стоп-слов # 
stop_words = set(stopwords.words('russian'))  # Стоп-слова 
words = nltk.word_tokenize(text)  # Токенизация текста 
without_stop_words = set([word for word in words if word not in stop_words and word.isalnum()]) 

# Морфологический разбор каждого слова # 
result = [] 
for word in without_stop_words: 
    p = morph.parse(word)[0] 
    result.append("Слово: " + word + "\nНормальная форма: " + str( 
        p.normal_form) + "\nМорфологический разбор слова: " + p.tag.cyr_repr + '\n\n') 
 
# Запись в файл # 
with open('morf_analyze.txt', 'w') as write_file: 
    write_file.write(''.join(result)) 