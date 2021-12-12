from table import Table
import matplotlib.pyplot as plt
import os


class TableCollection(object):
    def __init__(self):
        self.set_tables()
        self.check_tables()

    def __str__(self):
        s = str()
        for t in self.tables:
            s += "\n" + str(t)
        return s

    @property
    def tables(self):
        print("tables")
        return self._tables

    @tables.getter
    def tables(self):
        return self._tables

    def set_tables(self):
        self._tables = []
        list_files = os.listdir("datas")
        for f in list_files:
            category = f[:4]
            self._tables.append(Table("datas/"+f, category))

    @staticmethod
    def get_summary(matr):
        s = [0] * len(matr[0])
        for i in range(len(matr)):
            for j in range(len(matr[i])):
                s[j] += matr[i][j]
        return [i / len(matr) for i in s]

    def factor_results(self):
        categories = set()
        for cur in self.tables:
            categories.add(cur.category)
        std = {}
        for categ in categories:
            tmp = []
            for cur in self.tables:
                if cur.category == categ:
                    tmp.append(cur.standartize())
            std[categ] = TableCollection.get_summary(tmp)
        return std

    def output_factor_results(self):
        for k,v in self.factor_results().items():
            print(f"{k}:")
            v = list(v)
            for i in range(len(v)):
                print(f"{Table.names[i]}:  {v[i]}")

    def result(self):
        return TableCollection.get_summary(list(self.factor_results().values()))

    def output_result(self):
        v = self.result()
        for i in range(len(v)):
            print(f"{Table.names[i]}:  {v[i]}")

    def check_tables(self):
        d = {}
        for t in self.tables:
            if t.relation_sogl() > 0.15 or t.relation_sogl()<0:
                d[t.file] = False
        wrong_tables = []
        for k, v in d.items():
            if not v:
                wrong_tables.append(k)
        return wrong_tables
