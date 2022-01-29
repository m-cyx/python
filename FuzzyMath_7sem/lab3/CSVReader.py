from functools import reduce
import numpy as np


PSS_LIST = [0.0, 0.0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51, 1.48, 1.56, 1.57, 1.59]


class CSVReader:
    def __init__(self, filename):
        self.data = CSVReader.read_data_from_csv(filename)

    def get_geometric_mean(self):
        """Возвращает список со средне геометрическим каждой строки"""
        return [pow(reduce(lambda x, y: x * y, line), 1 / len(self.data)) for line in self.data]

    def get_nvp(self):
        """Расчет компонентов нормализованного вектора"""
        geometric_mean = self.get_geometric_mean()
        sum_geometric_mean = sum(geometric_mean)

        return [elem / sum_geometric_mean for elem in geometric_mean]

    def get_vector_priority(self):
        sum_matrix = 0
        for line in self.data:
            sum_matrix += sum(line)

        vector_priority = list(map(lambda x: sum(x)/sum_matrix, self.data))

        return list(map(lambda x: x / max(vector_priority), vector_priority))

    def set_lambda_max(self):
        """Возвращает максимальное собственное значение матрицы"""
        nvp_list = self.get_nvp()
        lambda_max = 0

        for i in range(len(self.data)):
            column = [line[i] for line in self.data]
            lambda_max += (sum(column) * nvp_list[i])

        return lambda_max

    def get_index_consistency(self):
        """Возвращает индекс согласованности"""
        return (self.set_lambda_max() - len(self.data)) / (len(self.data) - 1)

    def get_consistency_relation(self):
        """Возвращает отношение согласованности"""
        return self.get_index_consistency() / PSS_LIST[len(self.data)]

    @staticmethod
    def read_data_from_csv(filename):
        """Возвращает данные из таблицы cv, преобразуя в список списков с элементами типа float"""
        with open(f'data1/{filename}.csv') as file:
            rows = file.readlines()
            return [list(map(lambda x: float(x), row.split(';')[1:])) for row in rows[1:]]
