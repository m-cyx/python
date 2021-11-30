
#модуль контрол в документации посмотреть Его использовал Кирилл 
"""
В бд хранятся данные, которые мы вводим в поля для каждой лингвистической переменной.
По ним считается мат ожидание и средне квадратичное отклонение (два коэффицента сигма и а).
На основе этих двух коэфов строятся 3 графика для термов. Так три раза.
Во вьюшке ничего менять не надо, всё ок. Разобраться с библиотекой, бдшкой и модулем контрол. 
Ps. Вьюшки нет, бд - txt файл, всё записывается и читается норм, есть проверка ввода
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

import os
import numpy as np

# Чищу консольку
os.system('cls||clear')

 
# New Antecedent/Consequent objects hold universe variables & membership
# functions
zhelezo = ctrl.Antecedent(np.arange(0, 11, 1), 'zhelezo')
monitor = ctrl.Antecedent(np.arange(0, 11, 1), 'monitor')
pereferiya = ctrl.Antecedent(np.arange(0,11,1), 'pereferiya')
price = ctrl.Consequent(np.arange(0, 300, 1), 'price')


# !!!! ВОТ ТУТ НАДО ЗАДАВАТЬ КОЭФИЦЕНТЫ ГРАФИКОВ ДЛЯ ФУНКЦИЙ ПРИНАДЛЕЖНОСТИ !!!
# Auto-membership function population is possible with .automf(3, 5, or 7)
zhelezo.automf(3)
monitor.automf(3)
pereferiya.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
price['low'] = fuzz.trimf(price.universe, [0, 0, 40])
price['medium'] = fuzz.trapmf(price.universe, [0, 40, 90, 110])
price['high'] = fuzz.trimf(price.universe, [40, 160, 300])


# Определяю талицу правил
rule1 = ctrl.Rule(zhelezo['poor'] & monitor['poor'] & pereferiya ['poor'],         price['low'])
rule2 = ctrl.Rule(zhelezo['poor'] & monitor['poor'] & pereferiya ['average'],      price['low'])
rule3 = ctrl.Rule(zhelezo['poor'] & monitor['poor'] & pereferiya ['good'],         price['medium'])

rule4 = ctrl.Rule(zhelezo['poor'] & monitor['average'] & pereferiya ['poor'],      price['low'])
rule5 = ctrl.Rule(zhelezo['poor'] & monitor['average'] & pereferiya ['average'],   price['medium'])
rule6 = ctrl.Rule(zhelezo['poor'] & monitor['average'] & pereferiya ['good'],      price['medium'])

rule7 = ctrl.Rule(zhelezo['poor'] & monitor['good'] & pereferiya ['poor'],         price['medium'])
rule8 = ctrl.Rule(zhelezo['poor'] & monitor['good'] & pereferiya ['average'],      price['medium'])
rule9 = ctrl.Rule(zhelezo['poor'] & monitor['good'] & pereferiya ['good'],         price['medium'])


rule10 = ctrl.Rule(zhelezo['average'] & monitor['poor'] & pereferiya ['poor'],      price['low'])
rule11 = ctrl.Rule(zhelezo['average'] & monitor['poor'] & pereferiya ['average'],   price['low'])
rule12 = ctrl.Rule(zhelezo['average'] & monitor['poor'] & pereferiya ['good'],      price['medium'])

rule13 = ctrl.Rule(zhelezo['average'] & monitor['average'] & pereferiya ['poor'],   price['medium'])
rule14 = ctrl.Rule(zhelezo['average'] & monitor['average'] & pereferiya ['average'],price['medium'])
rule15 = ctrl.Rule(zhelezo['average'] & monitor['average'] & pereferiya ['good'],   price['medium'])

rule16 = ctrl.Rule(zhelezo['average'] & monitor['good'] & pereferiya ['poor'],      price['medium'])
rule17 = ctrl.Rule(zhelezo['average'] & monitor['good'] & pereferiya ['average'],   price['medium'])
rule18 = ctrl.Rule(zhelezo['average'] & monitor['good'] & pereferiya ['good'],      price['high'])


rule19 = ctrl.Rule(zhelezo['good'] & monitor['poor'] & pereferiya ['poor'],         price['high'])
rule20 = ctrl.Rule(zhelezo['good'] & monitor['poor'] & pereferiya ['average'],      price['high'])
rule21= ctrl.Rule(zhelezo['good'] & monitor['poor'] & pereferiya ['good'],          price['high'])

rule22= ctrl.Rule(zhelezo['good'] & monitor['average'] & pereferiya ['poor'],       price['high'])
rule23= ctrl.Rule(zhelezo['good'] & monitor['average'] & pereferiya ['average'],    price['high'])
rule24= ctrl.Rule(zhelezo['good'] & monitor['average'] & pereferiya ['good'],       price['high'])

rule25= ctrl.Rule(zhelezo['good'] & monitor['good'] & pereferiya ['poor'],          price['high'])
rule26 = ctrl.Rule(zhelezo['good'] & monitor['good'] & pereferiya ['average'],      price['high'])
rule27= ctrl.Rule(zhelezo['good'] & monitor['good'] & pereferiya ['good'],          price['high'])


#Now that we have our rules defined, we can simply create a control system via:
priceping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12,  rule13, rule14, rule15, rule16, rule17, rule18,  rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26,  rule27])

"""
In order to simulate this control system, we will create a
``ControlSystemSimulation``.  Think of this object representing our controller
applied to a specific set of cirucmstances.  For priceping, this might be priceping
Sharon at the local brew-pub.  We would create another
``ControlSystemSimulation`` when we're trying to apply our ``priceping_ctrl``
for Travis at the cafe because the inputs would be different.
"""

priceping = ctrl.ControlSystemSimulation(priceping_ctrl)

"""
We can now simulate our control system by simply specifying the inputs
& calling the ``compute`` method.  Suppose we rated the zhelezo 6.5 out of 10
& the monitor 9.8 of 10.
"""
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

#zhe = float(input('Введите уровень железа: '))
#mon = float(input('Введите уровень монитора: '))
#per = float(input('Введите уровень переферии: '))


# Ввод и проверка значений
while True:
    zhe = int(input('Железо: '))
    mon = int(input('Монитор: '))
    per = int(input('Периферия: '))
    if (zhe > 10) or (mon > 10) or (per > 10): 
        os.system('cls||clear')
        print('Пожалуйста, введите значения не превышающее 10.')
    else:
        break

priceping.input['zhelezo'] = zhe
priceping.input['monitor'] = mon
priceping.input['pereferiya'] = per


# Запускаю шайтан машину, компутирую
priceping.compute()


# Когда скомпутировано, то вывожу, можно так же визуализировать этот объект.
print('\n==========')
print( "Цена: " + str(round(priceping.output['price'])) + " тыс. рублей")
print('==========')


# Запись в файл
with open('db.txt', 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('zhe'):
            lines[i] = lines[i].strip() + ' ' + str(zhe) + '\n'
        elif line.startswith('mon'):
            lines[i] = lines[i].strip() + ' ' + str(mon) + '\n'
        elif line.startswith('per'):
            lines[i] = lines[i].strip() + ' ' + str(per) + '\n'
    f.seek(0)
    for line in lines:
        f.write(line)


# Чтение и создание списков, по которым будем считать 
with open('db.txt', 'r+') as f:
    vectors = []
    for eachLine in f:
        lst = eachLine.split()
        lst.remove(lst[0])
        vectors.append(lst)
zhel_vector = list(map(int, vectors[0]))
mon_vector = list(map(int, vectors[1]))
per_vector = list(map(int, vectors[2]))


# Среднее квадратичное по каждому вектору
std_zhel = np.std(zhel_vector)
std_mon = np.std(mon_vector)
std_per = np.std(per_vector)
print('\n==========')
print('Cреднее квадратичное по каждому верктору:')
print('По железу: ' + str(std_zhel))
print('По монитору: ' + str(std_mon))
print('По периферии: ' + str(std_per))
print('==========')


# Мат ожидание по каждому вектору
mean_zhel = np.mean(zhel_vector)
mean_mon = np.mean(mon_vector)
mean_per = np.mean(per_vector)
print('\n==========')
print('Мат ожидание по каждому вектору:')
print('По железу: ' + str(mean_zhel))
print('По монитору: ' + str(mean_mon))
print('По периферии: ' + str(mean_per))
print('==========')


# Списки из бд для отладки
#print('\nСписок железо: ' + str(zhel_vector))
#print('Список моник: ' + str(mon_vector))
#print('Список периферия: ' + str(per_vector))
