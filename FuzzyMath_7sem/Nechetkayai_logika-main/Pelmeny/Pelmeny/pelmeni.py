from tableCollection import TableCollection


def main():
    # print(file1.get_sheet_names())
    tables = TableCollection()
    if tables.check_tables():
        for cur in tables.check_tables():
            print(f"В {cur} нарушение согласованности. Пусть эксперт изменит свою оценку.")
    else:
        tables.output_factor_results()
        tables.output_result()
    # print(tables)


if __name__ == '__main__':
    main()