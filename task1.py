import random

import numpy as np
import pandas as pd
import IPython
from IPython.display import display


def print_csv(emp_df):
    print(emp_df)


def print_uniques_in_random_column(emp_df):
    random_column = emp_df.sample(axis='columns')
    print("Столбец: " + str(random_column.columns.values[0]))
    print("Уникальные значения:")
    print(np.unique(random_column.to_numpy()))


def print_nans_in_columns(emp_df):
    for column in emp_df:
        count_nan = emp_df[column].isna().sum().sum()
        print('Столбец : ', column, end='')
        print(' Количество NaN : ', count_nan)


def rename_random_column(emp_df, rename_to):
    random_column = emp_df.sample(axis='columns')
    random_column_name = str(random_column.columns.values[0])
    emp_df = emp_df.rename(columns={random_column_name: rename_to})
    return emp_df


def replace_last_column_to_first(emp_df):
    last_column_name = str(emp_df.columns.values[-1])
    last_column = emp_df[last_column_name]
    emp_df = emp_df.drop(columns=[last_column_name])
    emp_df.insert(0, last_column_name, last_column)
    return emp_df


def main():
    csv = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/park.csv"

    # 1.1. Загрузить данные в датафрейм с использованием функции read_csv.
    emp_df = pd.read_csv(csv)

    # 1.2. Вывести датафрейм на экран, описать в отчёте его содержание
    # (например: датафрейм содержит сведения о заёмщиках банка и включает следующие столбцы:
    #  Age - возраст
    #  Education – образованине
    #  и т.д. )
    print_csv(emp_df)

    # 1.3 Вывести первые 5 строк датафрейма
    print_csv(emp_df.head())

    # 1.4 Вывести всю информацию о датафрейме с использованием функции
    #  Info. Проанализировать полученную информацию.
    print_csv(emp_df.info())

    # 1.5 Вывести отдельно количество строк и столбцов
    print("Количество столбцов: " + str(len(emp_df.columns)))
    print("Количество строк: " + str(len(emp_df.index)))

    # 1.6 Вывести названия столбцов
    print(list(emp_df.columns))

    # 1.7 Вывести индексы строк
    print("Индексы строк")
    for i in emp_df.index:
        print(str(i) + ", ", end='')
    print("")

    # 1.8 Вывести содержимое датафрейма как массив.
    print(emp_df.to_numpy())

    # 1.9. Вывести типы данных в каждом столбце.
    print(list(emp_df.dtypes))

    # 1.10. Вывести массив уникальных значений в столбце (столбец выбирается
    # произвольно)
    print_uniques_in_random_column(emp_df)

    # 1.11 Вывести количество уникальных значений в каждом столбце датафрейма.
    print("Количество уникальных значений в каждом столбце датафрейма")
    print(emp_df.nunique())

    # 1.12 Вывести количество пропущенных значений в каждом столбце.
    print_nans_in_columns(emp_df)

    # 1.13 Удалить строки с пропущенными значениями.
    emp_df = emp_df.dropna()
    print(emp_df)

    # 1.14 Удалить дубликаты строк (при наличии).
    emp_df = emp_df.drop_duplicates()

    print(emp_df)

    # 1.15 Переименовать два произвольных столбца
    emp_df = rename_random_column(emp_df, "Виноград")
    emp_df = rename_random_column(emp_df, "Яблоко")
    print(emp_df[["Виноград", "Яблоко"]])

    # 1.16 Удалить последний столбец и вставить его в начало датафрейма (первым столбцом)
    emp_df = replace_last_column_to_first(emp_df)
    print(emp_df)
    # 1.16(VERSION 2). Удалить 20 последних строк датафрейма.
    emp_df = emp_df.drop(emp_df.tail(20).index)
    print(emp_df)
    # 1.17. Сформировать из исходного датафрейма датафрейм, содержащий 10 первых строк и 3 первых столбца.
    old_df = pd.read_csv(csv)
    new_df = old_df.head(10)
    new_df = pd.concat([new_df, old_df.tail(3)])
    print(new_df)
    # 1.18. Записать полученный датафрейм в файл EXCEL.
    new_df.to_excel("output.xlsx")


main()
