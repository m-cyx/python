import csv
import numpy as np


sluch_ind = [0., 0., 0.58, 0.9, 1.12,
             1.24, 1.32, 1.41, 1.45, 1.49,
             1.51, 1.48, 1.56, 1.57, 1.59]


class Table(object):
    names = []
    def __init__(self, f, cat):
        self.file = f
        self.category = cat
        self.set_table()
        self.set_lyambda()

    def __str__(self):
        return "Отношение согласованности " + str(self.relation_sogl()) + \
               " Lyambda: " + str(self.lyambda)+\
               " file: " + str(self.file)+\
               "\n" + str(self.table)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def lyambda(self):
        print("lyambda")
        return self._lyambda

    @lyambda.getter
    def lyambda(self):
        return self._lyambda

    def set_lyambda(self):
        self._lyambda = self.find_lyambda()

    @property
    def file(self):
        print("FILE")
        return self._file

    @file.setter
    def file(self, val):
        if isinstance(val, str):
            self._file = val
        else:
            return "Это не строка"

    @file.getter
    def file(self):
        return self._file

    @property
    def table(self):
        print("ТАБЛИЦА")
        return self._table

    @table.getter
    def table(self):
        return self._table

    def set_table(self):
        self._table = self.csv_read()

    @staticmethod
    def punktua(s):
        return ".".join(s.split(","))

    @staticmethod
    def change_lst(lst):
        for i in range(len(lst)):
            lst[i] = Table.punktua(lst[i])
        return lst

    def sred_geom(self):
        res_l = []
        for key, cur_l in self.table.items():
            res = 1
            for i in cur_l:
                res *= i
            res_l.append(res**(1/len(cur_l)))
        return res_l

    def standartize(self):
        res = []
        l = self.sred_geom()
        for cur in l:
            res.append(cur/sum(l))
        return res

    def get_names(self):
        return self.table.keys()

    def csv_read(self):
        with open(self.file, "r", newline='', encoding="windows-1251") as file:
            reader = csv.reader(file, delimiter=";")
            count = 0
            names = list()
            d = list()
            for i in reader:
                if count == 0:
                    names = i[1:]
                else:
                    d.append(list(map(float, Table.change_lst(i[1:]))))
                count += 1
            if not Table.names:
                Table.names = names
            data = dict()
            for i in range(len(names)):
                data[names[i]] = d[i]
            return data

    def get_matr_from_dict(self):
        res = list()
        for key, val in self.table.items():
            res.append(val)
        return res

    def find_lyambda(self):
        np_data = np.array(self.get_matr_from_dict())
        #print(np_data.shape)
        #print(np_data)
        w, v = np.linalg.eig(np_data)
        return round(max(w), 3)

    def ind_sogl(self):
        return (self.lyambda - len(self.table))/(len(self.table) - 1)

    def relation_sogl(self):
        return round(self.ind_sogl()/sluch_ind[len(self.table)], 3)