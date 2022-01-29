from CSVReader import CSVReader

sweetness = ('expert1_slad', 'nikita_slad', 'max_slad') # Эргономика \ сладость
ossicles = ('expert1_kost', 'nikita_kost', 'max_kost') # Надёжность \ косточки
peel = ('expert1_koz', 'nikita_koz', 'max_koz') # Красота \ кожура

# Таблица сравнения критериев
# Собственные значения вектора по каждой строке
# Расчёт НВП по каждому критерию (оценка важности критерия)
# Проверка согласованности

# Попарное сравнения вариантов по каждому критерию
# Определение общего критерия для каждого варианта
# Расчёт обобщённого отношения согласованности 
# Решение достоверно, если обобщ отн согл <= 10-15%

def main():
    # отношение согласованности
    for file_name in (sweetness + ossicles + peel):
        csv_file = CSVReader(file_name)
        consistency_relation = csv_file.get_consistency_relation()
        if consistency_relation > 0.15 or consistency_relation < 0:
            print(f'Таблица {file_name}.csv не согласована!')
        else:
            print('Таблица ' + file_name + ' согласована')

    common_list = [0 for i in range(5)]
    for factor in (sweetness, ossicles, peel):
        norm = [0 for i in range(5)]
        for file_name in factor:
            csv_file = CSVReader(file_name)
            own_vector = csv_file.get_vector_priority()
            norm = [x + y for x, y in zip(own_vector, norm)]
        norm = list(map(lambda x: x / 3, norm))
        #print(norm)
        common_list = [x + y for x, y in zip(common_list, norm)]
    print('============================================= \nИтог: ')
    common_list = list(map(lambda x: x / 3, common_list))
    print(common_list)


if __name__ == '__main__':
    main()
