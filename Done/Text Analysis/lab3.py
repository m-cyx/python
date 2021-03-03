import nltk 
# Обработка первого предложения 
def one(): 
    # Грамматика
    grammar = nltk.CFG.fromstring(""" 
    S -> NP VP 
    VP -> V NP | VP PP 
    PP -> P NP 
    NP -> Det N | Det N PP | "Путешественник" 
    V -> "шел" 
    Det -> "несколько" | "небольшими" 
    N -> "недель" | "остановками" 
    P -> "с" 
    """) 
    text = "Путешественник шел несколько недель с небольшими остановками" 
    words = nltk.word_tokenize(text) 
    # Деревья синтаксического разбора 
    trees = nltk.ChartParser(grammar) 
    # Вывод
    print("\t\t" + text) 
    for t in trees.parse(words): 
        print(t) 
# Обработка второго предложения 
def two(): 
    # Грамматика
    grammar = nltk.CFG.fromstring(""" 
    S -> NP VP 
    VP -> V NP | VP PP 
    PP -> P NP 
    NP -> Det N | Det N PP | "путешественник" 
    V -> "шел" 
    Det -> "Несколько" | "небольшими" 
    N -> "недель" | "остановками" 
    P -> "с" 
    """) 
    text = "Несколько недель с небольшими остановками шел путешественник" 
    words = nltk.word_tokenize(text)  

    # Деревья синтаксического разбора 
    trees = nltk.ChartParser(grammar)  

    # Вывод
    print("\t\t" + text) 
    for t in trees.parse(words): 
        print(t) 
#модуль обработки третьего предложения 
def three(): 
    # Грамматика
    grammar = nltk.CFG.fromstring(""" 
    S -> NP VP 
    VP -> V NP | VP PP 
    PP -> P NP 
    NP -> Det N | Det N PP | "Он" 
    V -> "бежал" 
    Det -> "воспрянув" | "мокрому" 
    N -> "асфальту" | "духом" 
    P -> "по" 
    """) 
    text = "Он бежал воспрянув духом по мокрому асфальту" 
    words = nltk.word_tokenize(text)  
    # Деревья синтаксического разбора  
    trees = nltk.ChartParser(grammar)  
    # Вывод
    print("\t\t" + text) 
    for t in trees.parse(words): 
        print(t) 


if __name__ == '__main__': 
    one() 
    two() 
    three() 

 